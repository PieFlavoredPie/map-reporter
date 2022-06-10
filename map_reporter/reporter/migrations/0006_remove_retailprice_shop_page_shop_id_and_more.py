# Generated by Django 4.0.4 on 2022-06-02 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0005_rename_ka_price_product_key_acc_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retailprice',
            name='shop',
        ),
        migrations.AddField(
            model_name='page',
            name='shop_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='reporter.shop'),
        ),
        migrations.AddField(
            model_name='retailprice',
            name='shop_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='reporter.shop'),
        ),
        migrations.AlterField(
            model_name='retailprice',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='reporter.product'),
        ),
    ]
