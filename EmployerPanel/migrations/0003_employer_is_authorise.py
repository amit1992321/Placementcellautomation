# Generated by Django 2.1.5 on 2019-04-07 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployerPanel', '0002_auto_20190407_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='is_authorise',
            field=models.BooleanField(default=False, null=True),
        ),
    ]