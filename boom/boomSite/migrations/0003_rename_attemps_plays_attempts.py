# Generated by Django 4.0.3 on 2022-04-26 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boomSite', '0002_alter_global_timefinish_alter_global_timeplayed_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plays',
            old_name='attemps',
            new_name='attempts',
        ),
    ]
