# Generated by Django 2.2.7 on 2020-02-17 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0017_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todoapi.note'),
        ),
    ]