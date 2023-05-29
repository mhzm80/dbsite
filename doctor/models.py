from django.db import models

# Create your models here.
class d_doctor(models.Model):
    Firstname=models.CharField(max_length=200)
    Lastname=models.CharField(max_length=200)
    Nathonalcode=models.CharField(max_length=200)
    Username=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    Skill=models.CharField(max_length=200)


    def __str__(self):
        return self.Nathonalcode


class loginlogin(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.username
