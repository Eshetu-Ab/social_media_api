# Generated by Django 5.1.1 on 2024-09-29 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='timestamp',
        ),
    ]
