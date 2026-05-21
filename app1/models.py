from django.db import models

# Create your models here.

class Student(models.Model):
    st_name = models.CharField(max_length=100)
    st_age = models.IntegerField()
    st_email = models.EmailField(max_length=50)
    st_number = models.IntegerField()

    def __str__(self):
        return self.st_name
    
class User(models.Model):
    us_name = models.CharField(max_length=50,null=True)
    us_age = models.IntegerField(max_length=10)
    us_email = models.EmailField(max_length=100, null=True)
    us_phone = models.IntegerField(max_length=14, null=True)

    def __str__(self):
        return self.us_name



    
