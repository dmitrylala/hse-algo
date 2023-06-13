from django.forms.models import model_to_dict
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import TaskForm
from .models import Result
from .utils import (
    compute_stats,
    solve_task,
    sort_options,
)


def index(request: HttpRequest):
    return render(request, "algo/index.html")


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

        return HttpResponseRedirect(reverse("algo:task_result", args=(result.pk,)))

    return render(request, "algo/task.html", {"form": task_form})


class ResultView(generic.DetailView):
    model = Result
    template_name = "algo/task_result.html"
    context_object_name = "task_result"


class ResultListView(generic.ListView):
    model = Result
    template_name = "algo/history.html"
    context_object_name = "results"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # statistics
        context.update(**compute_stats(context["object_list"]))

        # sorting options
        context.update(**sort_options())

        return context

    def get_queryset(self):
        queryset = Result.objects.all()
        order_by = self.request.GET.get("order_by")
        if order_by:
            return queryset.order_by(order_by)
        return queryset
