# Generated by Django 5.1 on 2024-08-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0016_remove_course_category_course_categories_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="categories",
            field=models.ManyToManyField(related_name="kurslar", to="courses.category"),
        ),
    ]