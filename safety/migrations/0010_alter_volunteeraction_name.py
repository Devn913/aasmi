# Generated by Django 3.2.9 on 2021-11-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safety', '0009_alter_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteeraction',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Event Name'),
        ),
    ]
