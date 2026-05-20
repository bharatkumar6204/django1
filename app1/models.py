from django.db import models

# Create your models here.

class Student(models.Model):
    st_name = models.CharField(max_length=100)
    st_age = models.IntegerField()
    st_email = models.EmailField(max_length=50)
    st_number = models.IntegerField()

    def __str__(self):
        return self.st_name


    
