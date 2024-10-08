# Generated by Django 5.1 on 2024-10-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0019_alter_course_categories"),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="images")),
            ],
        ),
    ]
