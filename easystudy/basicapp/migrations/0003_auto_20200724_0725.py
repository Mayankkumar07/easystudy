# Generated by Django 3.0.3 on 2020-07-24 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0002_userprofile_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='SOME STRING', max_length=128),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='SOME STRING', max_length=128),
        ),
    ]