# Generated by Django 4.0.4 on 2022-06-11 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='username',
            new_name='user',
        ),
    ]