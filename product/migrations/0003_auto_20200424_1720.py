# Generated by Django 3.0.5 on 2020-04-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200424_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='category_type',
            field=models.CharField(choices=[('FOOD', 'Food'), ('TEGNOLOGY', 'Tegnology'), ('HOUSEHOLDS_ITEMS', 'Households_Items'), ('CLOTHING', 'Clothing'), ('HYGIENE', 'Hygiene'), ('GAMES', 'Games'), ('MATERNITY', 'Maternity'), ('MEDICINE', 'Medicine'), ('STATIONERY', 'Stationery')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='state_type',
            field=models.CharField(choices=[('USED', 'Used'), ('NEW', 'New'), ('BROKEN', 'Broken')], default='', max_length=50),
        ),
    ]