# Generated by Django 3.2.7 on 2021-09-08 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_alter_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
