# Generated by Django 3.1 on 2020-08-21 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0002_auto_20200821_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='field',
            options={'ordering': ['id'], 'verbose_name': 'Field option', 'verbose_name_plural': 'Field options'},
        ),
        migrations.AlterUniqueTogether(
            name='field',
            unique_together={('name', 'alt_name')},
        ),
    ]
