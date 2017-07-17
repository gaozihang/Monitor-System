from django.db import models

# Create your models here.

class Host(models.Model):
	util = models.CharField(max_length=30, null=True)
	mac = models.CharField(max_length=30, null=True)
	ip = models.GenericIPAddressField(max_length=15)

