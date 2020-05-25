# Generated by Django 3.0.6 on 2020-05-25 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0002_payments_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentsString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='payments',
            name='string',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='receipts.PaymentsString'),
        ),
        migrations.AddField(
            model_name='status',
            name='string',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='receipts.StatusString'),
        ),
    ]
