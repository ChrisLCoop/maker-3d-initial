# Generated by Django 5.0.3 on 2024-03-26 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_productoimagen_options_producto_sku_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='sku',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]