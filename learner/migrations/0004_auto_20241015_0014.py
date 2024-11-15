# Generated by Django 3.1.14 on 2024-10-14 22:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20241015_0014'),
        ('academic', '0007_auto_20241015_0014'),
        ('learner', '0003_auto_20241009_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disability_type', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('accommodations', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=25)),
                ('relationship_with_learner', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Brother', 'Brother'), ('Uncle', 'Uncle'), ('Aunt', 'Aunt')], max_length=45)),
                ('phone_number', models.CharField(max_length=15)),
                ('place_of_employment', models.CharField(max_length=25)),
                ('work_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=15)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='address.address')),
            ],
        ),
        migrations.CreateModel(
            name='ParentGuardian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=25)),
                ('relationship_with_learner', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Brother', 'Brother'), ('Uncle', 'Uncle'), ('Aunt', 'Aunt')], max_length=45)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('work_number', models.CharField(max_length=15)),
                ('employment_place', models.CharField(max_length=25)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='address.address')),
            ],
        ),
        migrations.CreateModel(
            name='SupportDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='support_documents/')),
                ('description', models.TextField(blank=True, null=True)),
                ('upload_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='emergencycontactdetails',
            name='learner',
        ),
        migrations.AlterUniqueTogether(
            name='enrolledlearner',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='enrolledlearner',
            name='class_name',
        ),
        migrations.RemoveField(
            model_name='enrolledlearner',
            name='learner_record',
        ),
        migrations.RemoveField(
            model_name='guardianinfo',
            name='learner',
        ),
        migrations.RemoveField(
            model_name='learneraddressinfo',
            name='district',
        ),
        migrations.RemoveField(
            model_name='learneraddressinfo',
            name='union',
        ),
        migrations.RemoveField(
            model_name='learneraddressinfo',
            name='upazilla',
        ),
        migrations.RemoveField(
            model_name='learner',
            name='class_registration',
        ),
        migrations.RemoveField(
            model_name='learner',
            name='learner',
        ),
        migrations.RemoveField(
            model_name='learner',
            name='teacher',
        ),
        migrations.AddField(
            model_name='learner',
            name='birth_certificate_no',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learner',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learner',
            name='disability',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learner',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='learner',
            name='exited_programme',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='learner',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learner',
            name='home_language',
            field=models.CharField(choices=[('english', 'English'), ('zulu', 'Zulu'), ('xhosa', 'Xhosa'), ('afrikaans', 'Afrikaans'), ('pedi', 'Pedi'), ('tswana', 'Tswana'), ('sotho', 'Sotho'), ('tsonga', 'Tsonga'), ('swati', 'Swati'), ('venda', 'Venda'), ('ndebele', 'Ndebele'), ('other', 'Other')], default='english', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learner',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='learner',
            name='joined_programme',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='learner',
            name='name',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learner',
            name='nationality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academic.nationality'),
        ),
        migrations.AddField(
            model_name='learner',
            name='phone_no',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learner',
            name='photo',
            field=models.ImageField(default='', upload_to='learner-photos/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learner',
            name='race',
            field=models.CharField(choices=[('B', 'Black African'), ('W', 'White'), ('C', 'Coloured'), ('A', 'Asian/Indian'), ('O', 'Other')], default='B', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learner',
            name='surname',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AcademicInfo',
        ),
        migrations.DeleteModel(
            name='EmergencyContactDetails',
        ),
        migrations.DeleteModel(
            name='EnrolledLearner',
        ),
        migrations.DeleteModel(
            name='GuardianInfo',
        ),
        migrations.DeleteModel(
            name='PersonalInfo',
        ),
        migrations.DeleteModel(
            name='PreviousAcademicCertificate',
        ),
        migrations.DeleteModel(
            name='LearnerAddressInfo',
        ),
        migrations.AddField(
            model_name='supportdocument',
            name='learner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.learner'),
        ),
        migrations.AddField(
            model_name='parentguardian',
            name='learners',
            field=models.ManyToManyField(related_name='parents', to='learner.Learner'),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='learner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emergency_contact', to='learner.learner'),
        ),
        migrations.AddField(
            model_name='disability',
            name='learners',
            field=models.ManyToManyField(related_name='disabilities', to='learner.Learner'),
        ),
    ]