# Generated by Django 4.1.7 on 2023-03-13 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_product_slug_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
