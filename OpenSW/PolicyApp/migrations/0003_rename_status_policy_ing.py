# Generated by Django 5.1.3 on 2024-11-12 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PolicyApp', '0002_policy_content_policy_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='policy',
            old_name='status',
            new_name='ing',
        ),
    ]
