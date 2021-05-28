# Generated by Django 2.2.7 on 2020-02-20 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0022_auto_20200220_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('created_by', models.CharField(max_length=80)),
                ('assigned_to', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='image')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapi.note')),
            ],
        ),
    ]
