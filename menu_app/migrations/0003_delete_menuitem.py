# Generated by Django 5.0 on 2025-07-28 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_remove_menuitem_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]
