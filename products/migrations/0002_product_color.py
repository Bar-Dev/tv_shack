# Generated by Django 3.2.6 on 2021-08-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]