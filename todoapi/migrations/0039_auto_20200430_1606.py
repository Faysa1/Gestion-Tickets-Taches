# Generated by Django 2.2.7 on 2020-04-30 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0038_auto_20200430_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='Task',
        ),
        migrations.RemoveField(
            model_name='note',
            name='titre',
        ),
    ]
