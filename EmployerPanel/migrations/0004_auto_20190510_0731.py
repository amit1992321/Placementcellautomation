# Generated by Django 2.1.7 on 2019-05-10 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmployerPanel', '0003_employer_is_authorise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='authorise_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TpoPanel.TpoDetails'),
        ),
    ]