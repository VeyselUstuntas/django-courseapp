# Generated by Django 5.1 on 2024-08-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0010_alter_category_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, default="", editable=False, unique=True),
        ),
    ]
