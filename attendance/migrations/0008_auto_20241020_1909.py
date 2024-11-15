# Generated by Django 3.1.14 on 2024-10-20 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_auto_20241018_0151'),
        ('learner', '0010_learner_center'),
        ('attendance', '0007_auto_20241019_2231'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='learnerattendance',
            unique_together={('teacher', 'classroom', 'learner', 'date')},
        ),
    ]