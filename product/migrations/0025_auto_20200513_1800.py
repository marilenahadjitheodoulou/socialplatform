# Generated by Django 3.0.5 on 2020-05-13 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_auto_20200513_1714'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductCategory',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
