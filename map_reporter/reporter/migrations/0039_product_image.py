# Generated by Django 4.0.4 on 2022-06-16 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0038_manufacturer_remove_product_brand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='product_images'),
        ),
    ]
