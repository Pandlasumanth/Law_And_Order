from django.db import models

class Police_Station(models.Model):

    Name=models.CharField(max_length=50 ,primary_key=True)
    Zone=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
class Police_Officer(models.Model):
    Name=models.CharField(max_length=50 ,primary_key=True)
    Father_Name=models.CharField(max_length=50 )
    Date_Of_Birth=models.DateField()
    Designation=models.CharField(max_length=50 )
    Station_Name=models.ForeignKey(Police_Station,on_delete=models.CASCADE)
    Email_Id=models.EmailField(max_length=100)
    Password=models.CharField(max_length=50 )
class Detective(models.Model):
    Name = models.CharField(max_length=50)
    Father_Name = models.CharField(max_length=50)
    Date_Of_Birth = models.DateField()
    Designation = models.CharField(max_length=50)
    Email_Id = models.EmailField(max_length=100,primary_key=True)
    Password = models.CharField(max_length=50)
