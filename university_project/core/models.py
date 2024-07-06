from django.db import models
from django.contrib.auth.models import User

class Faculty(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.title

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    graduation_date = models.DateField()

    def __str__(self):
        return self.user.username

class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    description = models.TextField()
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


