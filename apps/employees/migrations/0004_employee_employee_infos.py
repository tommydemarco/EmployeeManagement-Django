# Generated by Django 3.1 on 2020-08-22 00:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_infos',
            field=ckeditor.fields.RichTextField(default='Text'),
            preserve_default=False,
        ),
    ]