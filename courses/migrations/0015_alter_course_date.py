# Generated by Django 5.1 on 2024-08-27 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0014_alter_course_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
    ]
