# Generated by Django 2.2.7 on 2020-02-18 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0020_note_piece'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assigned_to',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='titre',
            field=models.CharField(max_length=70),
        ),
    ]
