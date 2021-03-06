# Generated by Django 3.0.6 on 2020-05-25 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0003_auto_20200525_1306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymentsstring',
            options={'verbose_name': 'Строка', 'verbose_name_plural': 'Строки'},
        ),
        migrations.AlterModelOptions(
            name='statusstring',
            options={'verbose_name': 'Строка', 'verbose_name_plural': 'Строки'},
        ),
        migrations.RemoveField(
            model_name='payments',
            name='string',
        ),
        migrations.RemoveField(
            model_name='status',
            name='string',
        ),
        migrations.AddField(
            model_name='paymentsstring',
            name='payments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='receipts.Payments'),
        ),
        migrations.AddField(
            model_name='statusstring',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='receipts.Status'),
        ),
        migrations.AlterField(
            model_name='paymentsstring',
            name='string',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='statusstring',
            name='string',
            field=models.TextField(default=None),
        ),
    ]
