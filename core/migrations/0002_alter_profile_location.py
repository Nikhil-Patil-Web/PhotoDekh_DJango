# Generated by Django 4.2.2 on 2023-06-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]