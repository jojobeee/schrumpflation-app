# Generated by Django 4.2 on 2024-06-19 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_purchase_purchase_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supermarket',
            name='address',
        ),
        migrations.RemoveField(
            model_name='supermarket',
            name='city',
        ),
        migrations.RemoveField(
            model_name='supermarket',
            name='country',
        ),
        migrations.RemoveField(
            model_name='supermarket',
            name='postal_code',
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
    ]
