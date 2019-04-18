
from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$', views.some_method),
    url(r'^create/$', views.create),
    url(r'(?P<my_val>\d+)/$', views.show),
    url(r'(?P<my_val>\d+)/edit/$', views.edit),
    url(r'(?P<my_val>\d+)/delete/$', views.destroy),
]

