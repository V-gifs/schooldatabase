from django.db import models
from datetime import datetime


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class CertificateType(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Grade(models.Model):
    type = models.CharField(max_length=2)

    def __str__(self):
        return self.type

class Department(models.Model):
    name = models.CharField(max_length=400)
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    fullname = models.CharField(max_length=400)
    YearofGraduation = models.IntegerField()
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    CertificateType = models.ForeignKey(CertificateType, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname