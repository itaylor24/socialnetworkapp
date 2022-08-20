# Generated by Django 4.0.5 on 2022-06-16 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shouts', '0007_shout_thread_child'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shout',
            name='thread_child',
        ),
        migrations.AddField(
            model_name='shout',
            name='thread_child',
            field=models.ManyToManyField(null=True, related_name='thread_child_shout', to='shouts.shout'),
        ),
    ]