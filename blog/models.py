from django.db import models

# Create your models here.

class blog_new1(models.Model):
    Auther=models.CharField(max_length=200)
    Title=models.CharField(max_length=200)
    Context=models.TextField()
    Nationalcode=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.Auther