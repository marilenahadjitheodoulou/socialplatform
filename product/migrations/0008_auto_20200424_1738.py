# Generated by Django 3.0.5 on 2020-04-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20200424_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='category_UNU_code',
            field=models.CharField(default='', max_length=50, verbose_name='UNU key'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_image',
            field=models.FileField(default='', upload_to=''),
        ),
    ]