# Generated by Django 3.2.7 on 2021-12-30 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(default='1900-1-1', verbose_name='生日'),
        ),
    ]
