from django.db import models

# Create your models here.

class blog_new(models.Model):
    Auther=models.CharField(max_length=200)
    Title=models.CharField(max_length=200)
    Context=models.TextField()
    Date=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.Auther