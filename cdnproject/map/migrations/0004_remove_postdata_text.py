# Generated by Django 2.1.3 on 2019-10-10 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_postdata_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postdata',
            name='text',
        ),
    ]
