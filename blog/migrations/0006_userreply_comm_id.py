# Generated by Django 3.0.7 on 2021-01-31 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_usercomm_userreply'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreply',
            name='comm_id',
            field=models.IntegerField(default=0),
        ),
    ]