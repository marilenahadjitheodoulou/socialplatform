# Generated by Django 3.0.5 on 2020-05-08 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20200508_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_type', models.CharField(default='', max_length=50)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.ProductCategory')),
            ],
            options={
                'verbose_name': 'subcategory',
                'verbose_name_plural': 'subcategories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.Subcategory'),
            preserve_default=False,
        ),
    ]
