# Generated by Django 4.1.4 on 2022-12-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='City',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='apply',
            name='Country',
            field=models.CharField(max_length=25),
        ),
    ]