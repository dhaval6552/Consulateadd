# Generated by Django 2.0.3 on 2018-03-15 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysecondapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_nmae',
            new_name='first_name',
        ),
    ]
