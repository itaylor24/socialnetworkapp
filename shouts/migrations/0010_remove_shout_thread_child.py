# Generated by Django 4.0.5 on 2022-06-16 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shouts', '0009_alter_shout_thread_child'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shout',
            name='thread_child',
        ),
    ]
