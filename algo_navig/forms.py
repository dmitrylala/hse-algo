from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["a", "b", "c"]

        labels = {
            "a": "Чиcлo A",
            "b": "Чиcлo B",
            "c": "Чиcлo C",
        }
