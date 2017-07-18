from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class classes(models.Model):
    className = models.CharField(max_length=25, unique=True)
    
	
class students(models.Model):
	studentId = models.BigIntegerField(default='0')
	points = models.BigIntegerField(default=0)
	name = models.CharField(max_length=25, default='no Name')
	lastName = models.CharField(max_length=25, default='no Last Name')
	className = models.CharField(max_length=25, default='no Class')
	badges = JSONField(default='{}')
	data = JSONField(default='{}')

class badges(models.Model):
	data = JSONField()