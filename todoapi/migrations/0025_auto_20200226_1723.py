# Generated by Django 2.2.7 on 2020-02-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0024_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]