# Generated by Django 4.1.2 on 2022-11-01 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeproject', '0012_alter_timespend_punchin'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('employee', 'date')},
        ),
    ]
