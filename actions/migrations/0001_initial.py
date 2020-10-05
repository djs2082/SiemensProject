# Generated by Django 3.0.5 on 2020-10-05 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compartment', '0002_auto_20201005_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionsModel',
            fields=[
                ('action_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Action Name')),
                ('compartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compartment.CompartmentModel', verbose_name='Compartment Name')),
            ],
        ),
    ]
