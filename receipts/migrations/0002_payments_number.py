# Generated by Django 3.0.6 on 2020-05-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]