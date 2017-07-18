from django.conf.urls import url
from classes import views
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^student/$', views.student),
    url(r'^all/$', views.allPosts)
    
    
]