# Generated by Django 4.1.7 on 2023-03-28 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_item_order_line_total_item_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='stock',
            field=models.CharField(default='', max_length=100),
        ),
    ]
