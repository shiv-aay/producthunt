# Generated by Django 2.2.13 on 2020-06-28 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='votes_total',
            field=models.IntegerField(default=1),
        ),
    ]
