# Generated by Django 4.2.3 on 2023-07-25 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='completed',
            new_name='is_completed',
        ),
    ]
