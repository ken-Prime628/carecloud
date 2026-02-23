from django.db import models

# Create your models here. 

class patient(models.Model):
    firtname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    dateregistered = models.DateTimeField()
    medicalhistory = models.TextField()

    def __str__(self):
        return self.firtname + self.lastname     


class doctor(models.Model):
     firtname = models.CharField(max_length=200)
     lastname = models.CharField(max_length=50)
     spaecialization = models.CharField(max_length=100)
     phonenumber = models.CharField(max_length=10)
     email = models.EmailField()
     yoe = models.IntegerField()

     def __str__(self):
         return self.firtname + self.lastname  