# Generated by Django 3.1.13 on 2021-08-27 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0006_auto_20210827_1004'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='UserClient',
        ),
    ]
