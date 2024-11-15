# Generated by Django 3.1.14 on 2024-10-14 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learner', '0004_auto_20241015_0014'),
        ('attendance', '0005_auto_20241015_0056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learnerattendance',
            old_name='date',
            new_name='attendance_date',
        ),
        migrations.AlterUniqueTogether(
            name='learnerattendance',
            unique_together={('learner', 'attendance_date')},
        ),
    ]