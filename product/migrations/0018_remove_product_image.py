# Generated by Django 3.0.5 on 2020-04-24 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]