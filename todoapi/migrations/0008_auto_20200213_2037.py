# Generated by Django 2.2.7 on 2020-02-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0007_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='img',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='titre',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
