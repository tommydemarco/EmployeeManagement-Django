# Generated by Django 3.1 on 2020-08-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Field Name')),
                ('alt_name', models.CharField(max_length=20, verbose_name='Short Name')),
                ('in_use', models.BooleanField(default=True, verbose_name='In use')),
            ],
        ),
    ]
