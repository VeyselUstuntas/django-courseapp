# Generated by Django 5.1 on 2024-10-12 20:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0022_alter_course_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="date",
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
