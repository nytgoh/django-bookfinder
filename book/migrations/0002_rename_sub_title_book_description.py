# Generated by Django 4.1.6 on 2023-02-14 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='sub_title',
            new_name='description',
        ),
    ]
