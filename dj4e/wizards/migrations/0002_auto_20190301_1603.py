# Generated by Django 2.1.5 on 2019-03-01 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wizards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wizard',
            old_name='breed',
            new_name='house',
        ),
        migrations.RenameField(
            model_name='wizard',
            old_name='weight',
            new_name='power',
        ),
        migrations.RenameField(
            model_name='wizard',
            old_name='foods',
            new_name='spell',
        ),
    ]
