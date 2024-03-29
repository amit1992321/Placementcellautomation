# Generated by Django 2.1.7 on 2019-04-07 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TpoPanel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('industry_type', models.CharField(choices=[('NONE', 'None'), ('IT', 'IT'), ('BPO', 'BPO'), ('MANUFACTURING', 'Manufacturing'), ('MEDIA', 'Media'), (
                    'FINANCE', 'Finance'), ('MEDICAL', 'Medical'), ('CONSTRUCTION', 'Construction'), ('TELECOMMUNICATION', 'Telecommunication')], max_length=120)),
                ('company_name', models.CharField(max_length=120)),
                ('company_address', models.CharField(max_length=120)),
                ('registration_no', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=20)),
                ('alternate_mobile', models.CharField(max_length=20)),
                ('company_details', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='EmployerPanel.CompanyDetails')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('job_Profile', models.CharField(max_length=20)),
                ('job_vacancy', models.CharField(max_length=5)),
                ('job_description', models.TextField()),
                ('job_ctc', models.CharField(max_length=5)),
                ('interview_date', models.DateTimeField()),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False, null=True)),
                ('is_authrise', models.BooleanField(default=False, null=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('authorise_by', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to='TpoPanel.TpoDetails')),
                ('employer', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to='EmployerPanel.Employer')),
            ],
        ),
    ]
