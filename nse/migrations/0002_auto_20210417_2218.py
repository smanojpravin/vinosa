# Generated by Django 3.1.6 on 2021-04-17 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banknifty',
            name='entry',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='banknifty',
            name='signal',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='banknifty',
            name='target',
            field=models.CharField(max_length=100),
        ),
    ]
