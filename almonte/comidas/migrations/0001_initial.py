# Generated by Django 5.0.7 on 2024-08-07 10:19

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime.today)),
                ('dia_semana', models.CharField(choices=[('L', 'Lunes'), ('M', 'Martes'), ('X', 'Miércoles'), ('J', 'Jueves'), ('V', 'Viernes'), ('S', 'Sábado'), ('D', 'Domingo')], max_length=1)),
                ('desayuno', models.CharField(choices=[('N', 'Normal'), ('P', 'Pronto'), ('X', 'No desayuno'), ('E', 'Enfermo')], max_length=1)),
                ('comida', models.CharField(choices=[('N', 'Normal'), ('P', 'Pronto'), ('T', 'Tarde'), ('X', 'No como'), ('B', 'Bolsa'), ('E', 'Enfermo')], max_length=1)),
                ('cena', models.CharField(choices=[('N', 'Normal'), ('T', 'Tarde'), ('X', 'No ceno'), ('E', 'Enfermo')], max_length=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
