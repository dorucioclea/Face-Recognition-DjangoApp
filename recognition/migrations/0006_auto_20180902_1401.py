# Generated by Django 2.1 on 2018-09-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognition', '0005_auto_20180902_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='firstname',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastname',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
