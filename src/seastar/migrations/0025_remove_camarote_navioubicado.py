# Generated by Django 4.2.5 on 2023-11-30 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seastar', '0024_pasajero_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camarote',
            name='navioUbicado',
        ),
    ]