# Generated by Django 4.1.13 on 2024-02-12 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0007_alter_category_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="category",
            new_name="category_name",
        ),
    ]
