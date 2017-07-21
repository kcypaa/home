from django.db import models
from django import forms
from django.contrib.postgres.fields import JSONField
from pagedown.widgets import PagedownWidget
from django import forms

def background_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return './post_assets/post_{0}/background.jpg'.format(instance.id, filename)

class blog(models.Model):
	blogId = models.BigIntegerField(default='0')
	points = models.BigIntegerField(default=0)
	modifiedDate = models.DateField(auto_now=False, auto_now_add=False)
	title = models.CharField(max_length=100, default='title')
	slug = models.SlugField(max_length=100, default='slug')
	body = models.TextField(default='')
	description = models.CharField(max_length=180,null=True)
	posted = models.DateField(db_index=True, auto_now_add=True)
	category = models.ForeignKey('blog.Category')
	background = models.FileField(upload_to=background_directory_path,default='/')
	data = JSONField(default='{}')


class category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)
	color = models.CharField(max_length=100, db_index=True,default='#000000')


