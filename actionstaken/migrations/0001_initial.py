# Generated by Django 3.0.5 on 2020-10-05 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actions', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionsTakenModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Date Time')),
                ('action', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='actions.ActionsModel', verbose_name='Action')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.EmployeeModel', verbose_name='Employee Name')),
            ],
        ),
    ]
