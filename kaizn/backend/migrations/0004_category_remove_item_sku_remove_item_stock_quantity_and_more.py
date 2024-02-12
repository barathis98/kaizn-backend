# Generated by Django 4.1.13 on 2024-02-12 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0003_alter_item_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="item",
            name="sku",
        ),
        migrations.RemoveField(
            model_name="item",
            name="stock_quantity",
        ),
        migrations.RemoveField(
            model_name="item",
            name="tags",
        ),
        migrations.AddField(
            model_name="item",
            name="cost",
            field=models.DecimalField(decimal_places=2, default=123123, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="item",
            name="is_assembly",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="item",
            name="is_bundle",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="item",
            name="is_component",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="item",
            name="is_purchaseable",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="item",
            name="is_salable",
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name="StockItem",
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
                ("in_stock", models.IntegerField()),
                ("total_allocated", models.IntegerField()),
                ("allocated_to_builds", models.IntegerField()),
                ("allocated_to_sales", models.IntegerField()),
                ("available_stock", models.IntegerField()),
                ("incoming_stock", models.IntegerField()),
                ("net_stock", models.IntegerField()),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="backend.item"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="item",
            name="SKU",
            field=models.CharField(default=12345, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="backend.category"
            ),
        ),
    ]