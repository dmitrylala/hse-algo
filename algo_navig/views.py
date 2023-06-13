from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.template import Context, Template

from .models import Page


def first_page(_: HttpRequest):
    return redirect("algo_navig:page", 3)


def page(request: HttpRequest, pk: int):
    menu_items = (
        Page.objects.values("id", "navig", "navig_position")
        .filter(navig_position__gt=0)
        .order_by("-navig_position")
    )

    page = Page.objects.values().get(id=pk)

    page_context = Context({"stats": []}, autoescape=True)
    rendered_content = Template(page["content"]).render(context=page_context)

    context = {"pk": pk, "menu_items": menu_items, "page": page, "content": rendered_content}
    return render(request, "algo_navig/page.html", context)
