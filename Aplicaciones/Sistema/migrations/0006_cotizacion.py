# Generated by Django 4.0.6 on 2024-07-30 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0005_cliente_correo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ci_cli', models.CharField(max_length=15)),
                ('nombre_apellido', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]
