# Generated by Django 2.2.7 on 2020-03-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0031_auto_20200310_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etablissements',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
