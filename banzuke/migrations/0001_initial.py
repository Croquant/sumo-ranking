# Generated by Django 5.0.3 on 2024-04-01 21:46

import django.db.models.deletion
import ulid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rikishi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basho',
            fields=[
                ('slug', models.CharField(editable=False, max_length=6, primary_key=True, serialize=False)),
                ('year', models.PositiveSmallIntegerField()),
                ('month', models.PositiveSmallIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Torikumi',
            fields=[
                ('id', models.CharField(default=ulid.ULID, editable=False, max_length=26, primary_key=True, serialize=False)),
                ('day', models.PositiveSmallIntegerField()),
                ('basho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='torikumi', to='banzuke.basho')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='torikumi', to='rikishi.division')),
                ('east', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='east', to='rikishi.rikishi')),
                ('west', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='west', to='rikishi.rikishi')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='win', to='rikishi.rikishi')),
            ],
        ),
    ]
