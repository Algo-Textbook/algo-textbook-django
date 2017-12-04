from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.learn_home, name='learn_home'),
]