from django.db import models

# Create your models here.
class noskhe_h(models.Model):
    Uid=models.CharField(max_length=10)
    Ideadoctor=models.TextField()

    def __str__(self):
        return self.Uid