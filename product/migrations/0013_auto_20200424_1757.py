# Generated by Django 3.0.5 on 2020-04-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_productcategory_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='parent',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
