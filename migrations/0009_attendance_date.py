# Generated by Django 4.1.2 on 2022-11-01 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeproject', '0008_remove_attendance_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateField(default='2022-11-01', unique=True),
            preserve_default=False,
        ),
    ]