# Generated by Django 5.0.3 on 2024-03-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="finished_at",
            field=models.DateTimeField(null=True),
        ),
    ]
