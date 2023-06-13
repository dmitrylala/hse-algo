from django.forms.models import model_to_dict
from django.http import HttpRequest
from django.middleware.csrf import get_token
from django.shortcuts import redirect, render
from django.views import generic

from .forms import TaskForm
from .models import (
    Page,
    Result,
)
from .utils import (
    compute_stats,
    filter_options,
    render_content,
    solve_task,
    sort_options,
)


def index(request: HttpRequest):
    index_page_id = Page.objects.filter(context_type="IN").values("id")
    if not index_page_id:
        context = {
            "title": "No index",
            "content": "<h2>Cтpaницa index нe дo6aвлeнa!</h2>",
        }
        return render(request, "algo_navig/page.html", context)
    return redirect("algo_navig:page", index_page_id[0]["id"])


def task(request: HttpRequest, context):
    result_page = Page.objects.filter(context_type="TR").values()[0]

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

        context.update(
            title=result_page["title"],
            content=render_content(
                result_page["content"],
                {"task_result": result, "pk": context["pk"]},
            ),
        )

        return render(request, "algo_navig/page.html", context)

    context.update(
        content=render_content(
            context["content"],
            {
                "form": task_form,
                "csrf_token": get_token(request),
                "pk": context["pk"],
            },
        ),
    )
    return render(request, "algo_navig/page.html", context)


def task_result(request: HttpRequest, context):
    task_page = Page.objects.filter(context_type="TS").values()[0]
    latest_result = Result.objects.latest("id")

    context.update(
        content=render_content(
            context["content"],
            {"task_result": latest_result, "pk": task_page["id"]},
        ),
    )
    return render(request, "algo_navig/page.html", context)


class ResultListView(generic.ListView):
    model = Result
    template_name = "algo_navig/page.html"
    context_object_name = "results"
    init_context = {}

    def get_url_params(self):
        return {k: v[0] for k, v in dict(self.request.GET).items()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(pk=self.init_context["pk"])

        # statistics
        context.update(**compute_stats(context["object_list"]))

        # sorting options
        context.update(**sort_options())

        # filtering options
        context.update(**filter_options())

        self.init_context.update(
            content=render_content(
                self.init_context["content"],
                context,
            ),
        )

        return self.init_context

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


def page(request: HttpRequest, pk: int):
    menu_items = (
        Page.objects.values("id", "navig", "navig_position")
        .filter(navig_position__gt=0)
        .order_by("-navig_position")
    )

    page = Page.objects.filter(id=pk).values()[0]

    context = {
        "pk": pk,
        "menu_items": menu_items,
        "title": page["title"],
        "content": page["content"],
    }

    view_funcs = {
        "TS": task,
        "TR": task_result,
        "HI": ResultListView.as_view(init_context=context),
    }

    view_func = view_funcs.get(page["context_type"])
    if view_func:
        return view_func(request, context)

    return render(request, "algo_navig/page.html", context)
