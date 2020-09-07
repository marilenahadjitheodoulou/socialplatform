# Generated by Django 3.0.5 on 2020-08-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0037_auto_20200827_1853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinterest',
            old_name='product',
            new_name='wished_item',
        ),
        migrations.RemoveField(
            model_name='productinterest',
            name='description',
        ),
        migrations.AddField(
            model_name='productinterest',
            name='slug',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]