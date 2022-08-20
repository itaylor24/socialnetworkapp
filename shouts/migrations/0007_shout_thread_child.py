# Generated by Django 4.0.5 on 2022-06-16 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shouts', '0006_shout_thread_parent_alter_shout_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='shout',
            name='thread_child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='thread_child_shout', to='shouts.shout'),
        ),
    ]
