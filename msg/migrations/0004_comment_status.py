# Generated by Django 3.2.7 on 2022-03-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0003_auto_20220122_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.IntegerField(default=0, verbose_name='状态'),
        ),
    ]
