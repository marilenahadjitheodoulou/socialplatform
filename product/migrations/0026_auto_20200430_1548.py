# Generated by Django 3.0.5 on 2020-04-30 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_remove_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterUniqueTogether(
            name='productcategory',
            unique_together={('slug', 'parent')},
        ),
    ]