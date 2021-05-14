# Generated by Django 3.1.6 on 2021-04-18 04:51

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('nse', '0003_auto_20210417_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fathername', models.CharField(max_length=100)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
