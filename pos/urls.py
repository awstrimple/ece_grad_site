from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.program_of_study, name='index'),
    url(r'^thanks/', views.thanks, name='thanks'),
    ]
