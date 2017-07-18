from django.contrib import admin
from .models import *
# from django_markdown.admin import MarkdownModelAdmin
# admin.site.register(blog, MarkdownModelAdmin)

# Register your models here.
admin.site.register(blog)
admin.site.register(category)