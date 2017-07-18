from django.db import models
from django.contrib.postgres.fields import JSONField
from pagedown.widgets import PagedownWidget
from django import forms

class blog(models.Model):
	blogId = models.BigIntegerField(default='0')
	points = models.BigIntegerField(default=0)
	modifiedDate = models.DateField(auto_now=False, auto_now_add=False)
	title = models.CharField(max_length=100, default='title')
	slug = models.SlugField(max_length=100, default='slug')
	body = models.TextField()
	posted = models.DateField(db_index=True, auto_now_add=True)
	category = models.ForeignKey('blog.Category')
	data = JSONField(default='{}')

class category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)

