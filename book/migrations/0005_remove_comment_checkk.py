# Generated by Django 4.1.6 on 2023-02-21 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='checkk',
        ),
    ]
