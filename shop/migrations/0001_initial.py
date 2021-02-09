# Generated by Django 3.0.7 on 2021-01-25 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=50)),
                ('prod_desc', models.CharField(max_length=2000)),
                ('prod_price', models.CharField(max_length=50)),
                ('prod_cat', models.CharField(default='', max_length=40)),
                ('prod_sub_cat', models.CharField(max_length=70)),
                ('pub_date', models.DateField()),
                ('prod_image', models.ImageField(upload_to='shop/images')),
            ],
        ),
    ]
