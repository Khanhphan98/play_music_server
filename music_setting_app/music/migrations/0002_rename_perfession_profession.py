# Generated by Django 4.1.5 on 2023-01-30 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Perfession",
            new_name="Profession",
        ),
    ]