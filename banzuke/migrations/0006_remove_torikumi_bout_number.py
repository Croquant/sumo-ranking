# Generated by Django 5.0.3 on 2024-05-24 16:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("banzuke", "0005_remove_torikumi_id_torikumi_bout_number_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="torikumi",
            name="bout_number",
        ),
    ]