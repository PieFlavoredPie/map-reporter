# Generated by Django 4.0.4 on 2022-06-14 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0029_merge_20220610_1657'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
