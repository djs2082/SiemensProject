# Generated by Django 3.0.5 on 2020-10-05 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartModel',
            fields=[
                ('part_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=250, verbose_name='Part Description')),
                ('part_code', models.CharField(max_length=15, unique=True, verbose_name='Part Code')),
            ],
        ),
    ]