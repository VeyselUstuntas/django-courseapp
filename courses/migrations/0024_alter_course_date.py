# Generated by Django 5.1 on 2024-10-12 20:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0023_alter_course_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
