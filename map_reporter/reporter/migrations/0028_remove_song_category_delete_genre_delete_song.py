# Generated by Django 4.0.4 on 2022-06-10 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0027_alter_category_options_category_level_category_lft_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='category',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
