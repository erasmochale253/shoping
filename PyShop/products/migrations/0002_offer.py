# Generated by Django 3.2.8 on 2021-10-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
