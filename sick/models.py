from django.db import models

# Create your models here.


class sick(models.Model):
    Firstname=models.CharField(max_length=200)
    Lastname=models.CharField(max_length=200)
    Age=models.IntegerField(default=0)
    Nationalcode=models.CharField(max_length=200)
    City=models.CharField(max_length=200)
    Phonenumber=models.CharField(max_length=200)
    Email=models.EmailField()
    Context=models.TextField()
    Drname=models.CharField(max_length=200)
    Insurence=models.CharField(max_length=200)
    statuc=models.BooleanField(default=False)
    
    def __str__(self):
        return self.Nationalcode