# Generated by Django 2.2.6 on 2019-11-05 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='movie',
        ),
    ]
