# Generated by Django 4.0.8 on 2024-10-30 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', to='shop.product'),
        ),
    ]
