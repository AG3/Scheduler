from django.db import models

# Create your models here.
class Professor(models.Model):
    first_name = models.CharField(max_length=20)
    mid_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name+','+self.mid_name+','+self.last_name+','+self.email
