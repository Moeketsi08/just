# Generated by Django 3.1.14 on 2024-10-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='union',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='upazilla',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]