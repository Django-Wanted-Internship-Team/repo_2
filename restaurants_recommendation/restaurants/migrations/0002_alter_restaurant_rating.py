# Generated by Django 4.2.6 on 2023-11-02 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]