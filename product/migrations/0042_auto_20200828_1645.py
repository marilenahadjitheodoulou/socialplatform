# Generated by Django 3.0.5 on 2020-08-28 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0041_auto_20200828_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
    ]
