# Generated by Django 4.1.13 on 2024-02-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0006_stockitem_desired_stock_stockitem_min_stock_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
