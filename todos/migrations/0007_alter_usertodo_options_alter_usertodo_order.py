# Generated by Django 4.2.4 on 2023-08-02 09:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0006_alter_todo_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="usertodo",
            options={"ordering": ["order"]},
        ),
        migrations.AlterField(
            model_name="usertodo",
            name="order",
            field=models.PositiveSmallIntegerField(),
        ),
    ]
