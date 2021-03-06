# Generated by Django 3.2.10 on 2021-12-31 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_auto_20210607_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Orders',
            field=models.ManyToManyField(related_name='order', to='Orders.ProductOrdered', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='productordered',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='shipping_address',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
