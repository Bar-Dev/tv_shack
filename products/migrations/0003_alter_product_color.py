# Generated by Django 3.2.6 on 2021-08-16 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(default=True, max_length=254),
            preserve_default=False,
        ),
    ]
