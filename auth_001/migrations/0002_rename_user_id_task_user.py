# Generated by Django 4.2.2 on 2023-06-25 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_001', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='user_id',
            new_name='user',
        ),
    ]
