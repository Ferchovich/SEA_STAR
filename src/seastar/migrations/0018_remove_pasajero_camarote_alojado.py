# Generated by Django 4.2.5 on 2023-11-03 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seastar', '0017_alter_pasajero_tipo_documento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pasajero',
            name='camarote_alojado',
        ),
    ]
