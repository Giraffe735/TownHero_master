# Generated by Django 2.1.3 on 2019-10-10 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_remove_postdata_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postdata',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='postdata',
            old_name='longitude',
            new_name='lng',
        ),
    ]
