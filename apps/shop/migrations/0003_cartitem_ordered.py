# Generated by Django 3.2.8 on 2021-10-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='ordered',
            field=models.IntegerField(default=0),
        ),
    ]