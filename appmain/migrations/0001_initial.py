# Generated by Django 3.0.2 on 2020-02-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=255, verbose_name='Производитель')),
                ('model', models.CharField(max_length=255, verbose_name='Модель')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('transmission', models.SmallIntegerField(choices=[('manual', 'механика'), ('automat', 'автомат'), ('robot', 'робот')], default='manual', verbose_name='Коробка передач')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]
