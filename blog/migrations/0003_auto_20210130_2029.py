# Generated by Django 3.0.7 on 2021-01-30 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210130_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post2',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='post',
            name='post3',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='post',
            name='post1',
            field=models.CharField(max_length=20),
        ),
    ]
