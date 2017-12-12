from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.question_list, name='question_list'),
    url(r'^(?P<pk>\d+)$', views.question_detail, name='question_detail'),
    url(r'^question/new/$', views.question_new, name='question_new'),
    url(r'^question/(?P<pk>\d+)/edit/$', views.question_edit, name='question_edit'),

]