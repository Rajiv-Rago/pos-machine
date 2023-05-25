# Generated by Django 4.1.7 on 2023-03-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0006_alter_item_stock_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='stock_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]