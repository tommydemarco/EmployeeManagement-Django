# Generated by Django 3.1 on 2020-08-21 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20200821_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='skills',
            field=models.ManyToManyField(to='employees.Skill'),
        ),
    ]