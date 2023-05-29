from django.db import models

# Create your models here.

class survey_u(models.Model):
    context=models.TextField()
    Email=models.EmailField()
    Drname=models.CharField(max_length=200)
    

    def __str__(self):
        return self.Email
