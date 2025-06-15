from django.db import models

# Create your models here for the database
class Member(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=50)
    passwd = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    age = models.IntegerField()


    def __str__(self):
        return self.fname + ' ' + self.lname