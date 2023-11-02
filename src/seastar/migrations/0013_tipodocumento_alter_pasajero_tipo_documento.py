# Generated by Django 4.2.5 on 2023-10-25 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seastar', '0012_remove_cubierta_camarote_camarote_cubiertaubicada_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTipoDocumento', models.CharField(max_length=100, verbose_name='Tipo de Documento')),
                ('descripcionTipoDocumento', models.CharField(max_length=200, verbose_name='Descripción del Tipo de Documento')),
            ],
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='tipo_documento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seastar.tipodocumento'),
        ),
    ]
