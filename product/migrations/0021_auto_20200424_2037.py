# Generated by Django 3.0.5 on 2020-04-24 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_productsubcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productsubcategory',
            options={'verbose_name': 'product subcategory', 'verbose_name_plural': 'product subcategories'},
        ),
        migrations.RenameField(
            model_name='productsubcategory',
            old_name='subcategory',
            new_name='category',
        ),
    ]
