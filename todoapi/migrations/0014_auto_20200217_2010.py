# Generated by Django 2.2.7 on 2020-02-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0013_auto_20200217_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
