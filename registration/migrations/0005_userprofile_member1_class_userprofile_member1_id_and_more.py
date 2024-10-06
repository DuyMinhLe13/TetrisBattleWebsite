# Generated by Django 4.2.2 on 2023-07-14 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_userprofile_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='member1_class',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='member1_id',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='member1_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='member2_class',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='member2_id',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='member2_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='member3_class',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='member3_id',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='member3_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
