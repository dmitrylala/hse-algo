from django.db import models


class Task(models.Model):
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()

    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"a = {self.a}, b = {self.b}, c = {self.c}"


class Result(models.Model):
    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    is_increasing = models.BooleanField()
    is_decreasing = models.BooleanField()

    def __str__(self):
        return (
            f"A < B < C: {self.is_increasing}, "
            f"A > B > C: {self.is_decreasing}, "
            f"task: {self.task}"
        )
