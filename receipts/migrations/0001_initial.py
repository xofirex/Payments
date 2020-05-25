# Generated by Django 3.0.6 on 2020-05-25 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('IP', 'В обработке'), ('PD', 'Оплачено'), ('RF', 'Возврат'), ('DC', 'Отклонен')], default='IP', max_length=2)),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('purpose', models.TextField(blank=True, default=None, null=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='receipts.Status')),
            ],
            options={
                'verbose_name': 'Квитанция',
                'verbose_name_plural': 'Квитанции',
            },
        ),
    ]
