from django.conf.urls import url
from blog import views
from django.core.urlresolvers import reverse

urlpatterns = [
	url(r'^blog/all/$', views.allTitles)
	]