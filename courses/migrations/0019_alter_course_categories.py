# Generated by Django 5.1 on 2024-09-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0018_course_ishome_alter_course_isactive"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="categories",
            field=models.ManyToManyField(
                blank=True, related_name="kurslar", to="courses.category"
            ),
        ),
    ]
