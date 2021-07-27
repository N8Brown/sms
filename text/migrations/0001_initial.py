# Generated by Django 3.2.5 on 2021-07-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=14, unique=True)),
                ('email', models.CharField(max_length=254)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
