# Generated by Django 2.2.7 on 2020-02-17 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0019_auto_20200217_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='piece',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todoapi.piece'),
        ),
    ]