# Generated by Django 2.2.7 on 2020-03-10 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0032_auto_20200310_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='etablissement',
        ),
    ]
