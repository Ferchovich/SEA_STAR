# Generated by Django 4.2.5 on 2023-10-23 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seastar', '0009_estadocamarote_camaroteocupado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estadocamarote',
            name='camaroteOcupado',
        ),
    ]
