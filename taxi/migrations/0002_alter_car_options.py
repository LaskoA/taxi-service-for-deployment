# Generated by Django 4.0.2 on 2022-08-11 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['id']},
        ),
    ]
