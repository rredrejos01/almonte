from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

dias_semana = (
    ("L", "Lunes"),
    ("M", "Martes"),
    ("X", "Miércoles"),
    ("J", "Jueves"),
    ("V", "Viernes"),
    ("S", "Sábado"),
    ("D", "Domingo"),
)

tipo_comidas = (
    ("N", "Normal"),
    ("P", "Pronto"),
    ("T", "Tarde"),
    ("X", "No como"),
    ("B", "Bolsa"),
    ("E", "Enfermo"),

)

tipo_desayuno = (
    ("N", "Normal"),
    ("P", "Pronto"),
    ("X", "No desayuno"),
    ("E", "Enfermo"),
)

tipo_cena = (
    ("N", "Normal"),
    ("T", "Tarde"),
    ("X", "No ceno"),
    ("E", "Enfermo"),
)

class Dia(models.Model):
    fecha=models.DateField(default=datetime.today)
    dia_semana=models.CharField(max_length=1, choices=dias_semana)
    desayuno=models.CharField(max_length=1, choices=tipo_desayuno)
    comida=models.CharField(max_length=1, choices=tipo_comidas)
    cena=models.CharField(max_length=1, choices=tipo_cena)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)

