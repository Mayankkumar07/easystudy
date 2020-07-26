# Generated by Django 3.0.3 on 2020-07-24 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0003_auto_20200724_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='code',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default=' ', max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default=' ', max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(help_text='Contact Phone Number', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='state',
            field=models.CharField(default=' ', max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='street',
            field=models.CharField(max_length=256),
        ),
    ]