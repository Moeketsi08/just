# Generated by Django 3.1.14 on 2024-10-08 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_remove_learner_class_registration'),
        ('teacher', '0002_auto_20241005_1503'),
        ('learner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrolledlearner',
            old_name='learner',
            new_name='learner_record',
        ),
        migrations.RemoveField(
            model_name='guardianinfo',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='guardianinfo',
            name='father_occupation',
        ),
        migrations.RemoveField(
            model_name='guardianinfo',
            name='father_phone_no',
        ),
        migrations.RemoveField(
            model_name='guardianinfo',
            name='father_yearly_income',
        ),
        migrations.RemoveField(
            model_name='guardianinfo',
            name='mother_name',
        ),
        migrations.RemoveField(
            model_name='guardianinfo',
            name='mother_occupation',
        ),
        migrations.RemoveField(
            model_name='guardianinfo',
            name='mother_phone_no',
        ),
        migrations.AddField(
            model_name='academicinfo',
            name='joined_programme',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='academicinfo',
            name='learner_provice',
            field=models.CharField(choices=[('EC', 'Eastern Cape'), ('GP', 'Gauteng'), ('KZN', 'KwaZulu-Natal'), ('LP', 'Limpopo'), ('MP', 'Mpumalanga'), ('NC', 'Northern Cape'), ('NW', 'North West'), ('WC', 'Western Cape'), ('FS', 'Free State')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='emergencycontactdetails',
            name='learner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learner.personalinfo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='guardian_surname',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='guardian_work_no',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='place_of_work',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='learner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learner.personalinfo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='disability',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='home_language',
            field=models.CharField(choices=[('english', 'English'), ('zulu', 'Zulu'), ('xhosa', 'Xhosa'), ('afrikaans', 'Afrikaans'), ('pedi', 'Pedi'), ('tswana', 'Tswana'), ('sotho', 'Sotho'), ('tsonga', 'Tsonga'), ('swati', 'Swati'), ('venda', 'Venda'), ('ndebele', 'Ndebele'), ('other', 'Other')], default='other', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='race',
            field=models.CharField(choices=[('B', 'Black African'), ('W', 'White'), ('C', 'Coloured'), ('A', 'Asian/Indian'), ('O', 'Other')], default='other', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='surname',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=829606, unique=True),
        ),
        migrations.AlterField(
            model_name='guardianinfo',
            name='guardian_name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='nationality',
            field=models.CharField(choices=[('SA', 'South African'), ('ZW', 'Zimbabwe')], max_length=45),
        ),
        migrations.AlterUniqueTogether(
            name='enrolledlearner',
            unique_together={('class_name', 'learner_record')},
        ),
        migrations.CreateModel(
            name='Learner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.classregistration')),
                ('learner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.enrolledlearner')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='learners', to='teacher.teacher')),
            ],
        ),
        migrations.RemoveField(
            model_name='enrolledlearner',
            name='roll',
        ),
    ]