from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.learn_home, name='learn_home'),
    url(r'^understand/1', views.u1_definition, name='u1'),
    url(r'^understand/2', views.u2_computer, name='u2'),
    url(r'^understand/3', views.u3_importance, name='u3'),
    url(r'^understand/4', views.u4_conditions, name='u4'),
    url(r'^understand/5', views.u5_practice, name='u5'),
    url(r'^understand/test', views.u6_test, name='u6'),

]

