from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^upload$', views.upload,name="upload_data"),
	url(r'^(?P<ip>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)/$', views.chart, name='chart'),
	url(r'^multi$', views.multi, name='multi'),
	url(r'^$', views.index,name="index"),
]
