# Generated by Django 3.0.5 on 2020-08-31 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0044_wishlist_wished_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinterest',
            old_name='interested',
            new_name='ordered',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]