# Generated by Django 4.2.6 on 2023-11-04 06:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contacts', '0006_alter_contact_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='avatar',
            field=models.ImageField(
                blank=True,
                default='static/images/User Avatar.jpg',
                null=True,
                upload_to='media/avatars',
            ),
        ),
    ]
