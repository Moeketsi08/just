# Generated by Django 3.1.14 on 2024-10-09 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20241005_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherqualification',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='TeacherPerformance',
        ),
        migrations.DeleteModel(
            name='TeacherQualification',
        ),
    ]
