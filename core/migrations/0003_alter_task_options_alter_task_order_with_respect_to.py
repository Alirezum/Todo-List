# Generated by Django 5.0.7 on 2024-07-25 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_task_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AlterOrderWithRespectTo(
            name='task',
            order_with_respect_to='user',
        ),
    ]