# Generated by Django 3.1.6 on 2021-02-11 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
    ]
