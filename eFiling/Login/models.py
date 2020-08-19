from django.db import models


# Create your models here.

class login(models.Model):
    object = None

    file = models.FileField(upload_to='file')
