# Generated by Django 3.0.5 on 2020-05-08 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20200508_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='parent_category',
        ),
    ]