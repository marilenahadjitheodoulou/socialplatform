# Generated by Django 3.0.5 on 2020-08-31 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0046_productinterest_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
