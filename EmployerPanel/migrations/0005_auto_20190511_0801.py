# Generated by Django 2.1.7 on 2019-05-11 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmployerPanel', '0004_auto_20190510_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='authorise_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TpoPanel.TpoDetails'),
        ),
    ]
