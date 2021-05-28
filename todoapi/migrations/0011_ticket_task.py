# Generated by Django 2.2.7 on 2020-02-17 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0010_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='Task',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='todoapi.Task'),
            preserve_default=False,
        ),
    ]