# Generated by Django 2.2.7 on 2020-03-10 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0035_auto_20200310_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='etablissement',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='todoapi.Etablissements', verbose_name='Series'),
        ),
    ]
