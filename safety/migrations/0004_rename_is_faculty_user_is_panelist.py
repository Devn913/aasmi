# Generated by Django 3.2.9 on 2021-11-13 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('safety', '0003_user_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_faculty',
            new_name='is_panelist',
        ),
    ]
