# Generated by Django 5.0.3 on 2024-05-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("banzuke", "0003_alter_basho_options_alter_torikumi_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="basho",
            name="end_date",
            field=models.DateField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="basho",
            name="start_date",
            field=models.DateField(blank=True, editable=False, null=True),
        ),
    ]