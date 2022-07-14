# Generated by Django 4.0.5 on 2022-07-04 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reporter', '0049_product_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='key_acc_price',
        ),
        migrations.AddField(
            model_name='shop',
            name='seller',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
