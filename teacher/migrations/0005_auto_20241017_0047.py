# Generated by Django 3.1.14 on 2024-10-16 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center_manager', '0003_auto_20241015_0014'),
        ('academic', '0010_auto_20241015_2052'),
        ('teacher', '0004_auto_20241015_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='center',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='center_manager.center'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='grade_taught',
            field=models.ManyToManyField(to='academic.Grade'),
        ),
    ]
