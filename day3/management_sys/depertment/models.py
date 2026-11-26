from django.db import models

# Create your models here.
class Institution(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=100)

    def __str__(self):
        return f'Institution: {self.name} Located: {self.location}'

class Employee(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    job_code = models.CharField(blank=False, max_length=10)
    email = models.EmailField(unique=True)
    depertment = models.ManyToManyField(
        'Depertment', blank=True, related_name='employees'
    )

    def __str__(self):
        return f"{self.first} {self.last} "
class Depertment(models.Model):
    name = models.CharField(max_length=100, unique=True)
    depertment_code = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # since in our shell when we run the Depertment.object.all() we don't get the string display of our model
    def __str__(self):
        return f" Office:{self.name} Code: {self.depertment_code}  Tel No: {self.phone_number}"


