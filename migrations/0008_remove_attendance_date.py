# Generated by Django 4.1.2 on 2022-11-01 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeproject', '0007_attendance_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='date',
        ),
    ]
