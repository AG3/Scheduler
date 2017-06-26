from django.db import models

# Create your models here.
class Course(models.Model):
    CRN = models.CharField(max_length=6)
    Subj = models.CharField(max_length=4)
    Crse = models.CharField(max_length=6)
    Sec = models.CharField(max_length=6)
    Cred = models.CharField(max_length=6)
    Title = models.CharField(max_length=50)
    Days = models.CharField(max_length=7)
    Time_begin = models.CharField(max_length=5)
    Time_end = models.CharField(max_length=5)
    Instructor = models.CharField(max_length=50)
    Location = models.CharField(max_length=15)
    Attribute = models.CharField(max_length=30)
    def __str__(self):
        return self.CRN+","+self.Subj+","+self.Crse+","+self.Instructor
