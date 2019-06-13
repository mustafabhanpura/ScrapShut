from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Detail(models.Model):
    name=models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=70,blank=True)
    phone_number = models.CharField(max_length=10,blank=True)
    image = models.FileField(upload_to='pic_folder/')
    video = models.FileField(upload_to='videos/')
    stream = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.name
