from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^home$', views.index),
    url(r'^add/(?P<user_id>\d+)$', views.add),
    url(r'^remove/(?P<friend_id>\d+)$', views.remove),
    url(r'^(?P<emailuser>.+)$', views.show),
]
