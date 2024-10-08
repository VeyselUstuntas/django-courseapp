# Generated by Django 5.1 on 2024-08-27 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0006_alter_course_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="courses.category",
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="slug",
            field=models.SlugField(blank=True, default="", editable=False, unique=True),
        ),
    ]
