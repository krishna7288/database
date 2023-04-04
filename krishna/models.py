from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=20,default="")
    age=models.IntegerField(default="")
    address=models.CharField(max_length=20,default="")
    mail=models.EmailField(max_length=30,default="")
    
    class Meta:
       db_table='krishna_register'

class File(models.Model):
    filename=models.CharField(max_length=20,default="")
    myfile=models.FileField()
    class Meta:
       db_table='file'
       
class Push(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    publish = models.BooleanField(max_length=10000)
    class Meta:
        db_table='publish'
        
        
       
class Table(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    publish = models.BooleanField(max_length=10000)
    class Meta:
        db_table='publisher'        

       
    
    