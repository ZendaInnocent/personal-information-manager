# Generated by Django 4.2.4 on 2023-09-09 20:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('todos', '0002_alter_todo_created_at_alter_todo_is_completed_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='todo',
            name='order',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='is completed'),
        ),
        migrations.DeleteModel(
            name='UserTodo',
        ),
    ]
