from django.db import models

# Create your models here.

#Creating Company Model

class Company(models.Model):
    companyId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=
                            (('IT','IT'),
                             ('Non IT','Non IT'),
                             ('Mobiles Phones','Mobiles Phones'),
                             ))
    addedDate = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

#Creating Employee Model

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=(
        ('Manager','manager'),
        ('SDE-2','sde-2'),
        ('SDE-1','sde-1'),
        ('Application Engineer','AE')
    ))
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
