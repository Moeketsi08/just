# Generated by Django 3.1.14 on 2024-10-07 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_auto_20241005_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='subject',
            field=models.CharField(choices=[('Mathematics', 'Mathematics'), ('Mathematics Exam', 'Mathematics Examination'), ('Physical Science', 'Physical Science'), ('Physical Science Exam', 'Physical Science Examination')], default='Mathematics', max_length=21),
        ),
        migrations.AlterField(
            model_name='session',
            name='day',
            field=models.CharField(choices=[('SAT', 'Saturday'), ('SUN', 'Sunday'), ('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THUR', 'Thursday'), ('FRI', 'Friday')], default='SAT', max_length=4),
        ),
        migrations.AlterUniqueTogether(
            name='classinfo',
            unique_together=set(),
        ),
    ]