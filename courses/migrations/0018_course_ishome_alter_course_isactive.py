# Generated by Django 5.1 on 2024-09-11 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0017_alter_course_categories"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="isHome",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="course",
            name="isActive",
            field=models.BooleanField(default=False),
        ),
    ]
