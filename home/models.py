from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    subject=models.CharField(max_length=122)
    Email=models.EmailField(max_length=122)
    message=models.CharField(max_length=122)
    def __str__(self):
        return self.name

class Appointment(models.Model):
    name=models.CharField(max_length=122)
    gender=models.CharField(max_length=122)
    Email=models.EmailField(max_length=122)
    date_time=models.CharField(max_length=122)
    time=models.CharField(max_length=122,null=True)
    

    def __str__(self):
        return self.nameexit