# Generated by Django 3.0.2 on 2020-01-04 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]