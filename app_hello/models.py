from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    interests = models.TextField(null=True)


class Experience(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, null=True)
    location = models.CharField(max_length=70, null=True)
    duration = models.CharField(max_length=70, null=True)
    position = models.CharField(max_length=70, null=True)
    job_discription = models.CharField(max_length=70, null=True)


class Education(models.Model): 
    DEGREE_CHOISES =[
        ("diploma","Diploma"),
        ("associate","Asociate deegree"),
        ("bachelor","Bachelor's degree"),
        ("master","Master's degree"),
        ("phd","Phd"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=70, null=True)
    location = models.CharField(max_length=70, null=True)
    duration = models.CharField(max_length=70, null=True)
    degree = models.CharField(max_length=70, null=True, choices=DEGREE_CHOISES)
    study_discription = models.CharField(max_length=70, null=True)

    @property
    def pretified_degree(self):
        return dict(self.DEGREE_CHOISES).get(self.degree)
