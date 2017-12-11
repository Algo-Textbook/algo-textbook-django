from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.learn_home, name='learn_home'),
]