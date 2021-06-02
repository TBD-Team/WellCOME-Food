from django.db import models
from django.contrib.auth.models import AbstractUser

from cpf_field.models import CPFField


class User(AbstractUser):
    STUDENT = 1
    PROFESSOR = 2
    TECHNICIAN = 3
    OUTSOURCED = 4
    ADM = 5
    ROLES = (
        (STUDENT, "Student"),
        (PROFESSOR, "Professor"),
        (TECHNICIAN, "Technician"),
        (OUTSOURCED, "Outsourced"),
        (ADM, "Administrator"),
    )

    email = models.EmailField(unique=True, null=False)
    role = models.PositiveSmallIntegerField(choices=ROLES, default=STUDENT)
    cpf = CPFField('cpf')

    def __str__(self):
        return self.username

    @property
    def is_student(self):
        return self.role == self.STUDENT

    @property
    def is_professor(self):
        return self.role == self.PROFESSOR

    @property
    def is_technician(self):
        return self.role == self.TECHNICIAN

    @property
    def is_outsourced(self):
        return self.role == self.OUTSOURCED

    @property
    def is_adm(self):
        return self.role == self.ADM
