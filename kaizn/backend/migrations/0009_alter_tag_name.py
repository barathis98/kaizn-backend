# Generated by Django 4.1.13 on 2024-02-12 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0008_rename_category_item_category_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
