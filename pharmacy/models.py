from django.db import models

# Create your models here.
class ph(models.Model):
    name=models.CharField(max_length=200)
    context=models.TextField()
    tedad=models.IntegerField(default=0)

    def __str__(self):
        return self.name