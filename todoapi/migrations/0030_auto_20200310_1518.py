# Generated by Django 2.2.7 on 2020-03-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0029_auto_20200310_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etablissement',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
