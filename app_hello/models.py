from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)


class Experience(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, null=True)
    location = models.CharField(max_length=70, null=True)
    duration = models.CharField(max_length=70, null=True)
    position = models.CharField(max_length=70, null=True)
    job_discription = models.CharField(max_length=70, null=True)