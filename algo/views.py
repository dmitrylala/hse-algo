from django.forms.models import model_to_dict
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import generic

from .forms import TaskForm
from .models import Result
from .utils import (
    compute_stats,
    filter_options,
    solve_task,
    sort_options,
)


def index(request: HttpRequest):
    return render(request, "algo/index.html")


def empty_history(request: HttpRequest):
    return render(request, "algo/empty_history.html")


def task(request: HttpRequest):
    post_data = request.POST or None
    task_form = TaskForm(post_data)
    if task_form.is_valid():
        task = task_form.save()

        # solving task and saving results
        task_conditions = model_to_dict(task)
        task_conditions.pop("id")
        is_increasing, is_decreasing = solve_task(**task_conditions)
        result = Result(task=task, is_increasing=is_increasing, is_decreasing=is_decreasing)
        result.save()

        return redirect("algo:task_result", result.pk)

    return render(request, "algo/task.html", {"form": task_form})


class ResultView(generic.DetailView):
    model = Result
    template_name = "algo/task_result.html"
    context_object_name = "task_result"


class ResultListView(generic.ListView):
    model = Result
    template_name = "algo/history.html"
    context_object_name = "results"

    def get(self, *args, **kwargs):
        if not Result.objects.exists():
            return redirect("algo:empty_history")
        return super().get(*args, **kwargs)

    def get_url_params(self):
        return {k: v[0] for k, v in dict(self.request.GET).items()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # statistics
        context.update(**compute_stats(context["object_list"]))

        # sorting options
        context.update(**sort_options())

        # filtering options
        context.update(**filter_options())

        return context

    def get_queryset(self):
        queryset = Result.objects.all()
        url_params = self.get_url_params()

        order_by = url_params.get("order_by")
        if order_by:
            return queryset.order_by(order_by)

        filter_by = url_params.get("filter_by")
        if filter_by:
            return queryset.filter(**{filter_by: True})

        return queryset
