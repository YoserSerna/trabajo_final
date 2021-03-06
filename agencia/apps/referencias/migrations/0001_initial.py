# Generated by Django 3.2.9 on 2021-11-25 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('viajeros', '0001_initial'),
        ('viajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
                ('telefono', models.CharField(max_length=100, verbose_name='Telefono')),
                ('viaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viajes.viaje')),
                ('viajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viajeros.viajero')),
            ],
            options={
                'verbose_name': 'Referencia',
                'verbose_name_plural': 'Referencias',
            },
        ),
    ]
