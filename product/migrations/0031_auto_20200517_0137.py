# Generated by Django 3.0.5 on 2020-05-16 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0030_remove_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(default=1, upload_to='media'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]