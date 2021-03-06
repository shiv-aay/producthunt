# Generated by Django 2.2.13 on 2020-06-28 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.SlugField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('votes_total', models.IntegerField(default=0)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='images/')),
                ('icon', models.ImageField(blank=True, default='defaulticon.png', upload_to='images/')),
            ],
        ),
    ]
