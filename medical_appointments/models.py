import uuid
from enum import Enum
from django.db import models


class MedicalAppointment(models.Model):
    class AppointmentTypes(models.TextChoices):
        CONSULTA = 'C', 'Consulta'
        SERVICIO = 'S', 'Servicio'
        TRATAMIENTO = 'T', 'Tratamiento'
        ESTUDIO = 'E', 'Estudios'
        LABORATORIO = 'L', 'Laboratorio'

    id = models.AutoField(verbose_name='ID', primary_key=True,)
    patient = models.CharField(verbose_name='Paciente', max_length=150)
    appointment_type = models.CharField(verbose_name='Tipo de Cita', max_length=50, choices=AppointmentTypes.choices)
    doctor_name = models.CharField(verbose_name='Nombre de médico que asiste', max_length=100)
    appointment_date = models.DateTimeField(verbose_name='Fecha y hora de la Cita')
    status = models.CharField(verbose_name="Estatus de Cita", default="Activa", max_length=100)
    is_active = models.BooleanField(verbose_name="Activo", default=True)
    creation_date = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)

    @property
    def appointment_number(self):
        return self.appointment_type + f'{self.id}'.zfill(12)

    def __str__(self):
        return self.appointment_number
