# Generated by Django 4.0.6 on 2024-07-20 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0002_alter_producto_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='productos'),
        ),
    ]
