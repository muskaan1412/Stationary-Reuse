# Generated by Django 3.1.2 on 2021-03-07 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adsphotosmodel',
            old_name='photos',
            new_name='photo',
        ),
    ]
