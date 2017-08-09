from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='index'),
    url('map/$', views.map, name='map'),
    url('exp/$', views.exp, name='exp'),
]
