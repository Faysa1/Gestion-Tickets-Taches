# Generated by Django 2.2.7 on 2020-03-10 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0034_delete_etablissements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etablissements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='etablissement',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='todoapi.Etablissements'),
            preserve_default=False,
        ),
    ]
