# Generated by Django 3.0.5 on 2020-09-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0050_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='received_from_my_place',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]