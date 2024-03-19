from django.db import models

# Create your models here.



class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(default='')

    email =  models.EmailField(default='',blank=True,null=True)

    # resume = models.FileField(upload_to='resumes')
 