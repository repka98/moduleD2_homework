# Generated by Django 4.1.2 on 2022-10-25 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='rating',
            new_name='ratingAuthor',
        ),
    ]
