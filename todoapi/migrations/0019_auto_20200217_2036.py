# Generated by Django 2.2.7 on 2020-02-17 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0018_task_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='piece jointe')),
            ],
        ),
        migrations.RemoveField(
            model_name='note',
            name='img',
        ),
    ]
