# Generated by Django 2.0.2 on 2019-04-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0002_event_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fee',
            field=models.IntegerField(default=100, max_length=3),
        ),
    ]
