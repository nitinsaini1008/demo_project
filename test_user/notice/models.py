from django.db import models

# Create your models here.

class notification(models.Model):
	subject=models.CharField(max_length=100)
	message=models.CharField(max_length=200)

