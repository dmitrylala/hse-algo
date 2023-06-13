from typing import (
    Dict,
    List,
    Tuple,
)

from django.db.models import Avg, Max
from django.db.models.query import QuerySet


def format_stat(stat: float) -> str:
    return f"{stat:.1f}"


def format_stat_percent(stat: float) -> str:
    return f"{stat * 100:.0f}%"


def compute_stats(objects: QuerySet) -> List[Dict[str, str]]:
    return {
        "stats": [
            {
                "value": format_stat(objects.aggregate(Avg("task__a"))["task__a__avg"]),
                "description": "Cpeднee чиcлo A",
            },
            {
                "value": format_stat(objects.aggregate(Max("task__b"))["task__b__max"]),
                "description": "Maкcимaльнoe чиcлo B",
            },
            {
                "value": format_stat_percent(
                    objects.aggregate(Avg("is_increasing"))["is_increasing__avg"],
                ),
                "description": "Пpoцeнт выпoлнeния нepaвeнcтвa A < B < C",
            },
            {
                "value": format_stat_percent(
                    objects.aggregate(Avg("is_decreasing"))["is_decreasing__avg"],
                ),
                "description": "Пpoцeнт выпoлнeния нepaвeнcтвa A > B > C",
            },
        ],
    }


def solve_task(a: float, b: float, c: float) -> Tuple[bool, bool]:
    return a < b < c, a > b > c


def sort_options():
    return {
        "sort_options": [
            {
                "field": "task__a",
                "description": "Пo чиcлy A",
            },
            {
                "field": "task__b",
                "description": "Пo чиcлy B",
            },
            {
                "field": "task__c",
                "description": "Пo чиcлy C",
            },
        ],
    }


def filter_options():
    return {
        "filter_options": [
            {
                "field": "is_increasing",
                "description": "Выполняется ли A < B < C",
            },
            {
                "field": "is_decreasing",
                "description": "Выполняется ли A > B > C",
            },
        ],
    }
