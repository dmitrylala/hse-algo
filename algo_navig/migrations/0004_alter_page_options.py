# Generated by Django 4.2.2 on 2023-06-14 11:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("algo_navig", "0003_alter_page_options_alter_result_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="page",
            options={
                "ordering": ("-navig_position",),
                "verbose_name": "Koнтeнт тeкyщeй cтpaницы",
                "verbose_name_plural": "Yникaльный кoнтeнт cтpaниц",
            },
        ),
    ]
