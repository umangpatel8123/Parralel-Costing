# Generated by Django 4.0.6 on 2022-10-21 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hetul11', '0004_alter_product_amazon_id_alter_product_filpkart_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amazon_id',
            field=models.CharField(default='', max_length=700),
        ),
        migrations.AlterField(
            model_name='product',
            name='filpkart_id',
            field=models.CharField(default='', max_length=700),
        ),
    ]
