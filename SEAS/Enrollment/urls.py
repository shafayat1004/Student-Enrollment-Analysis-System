from django.urls import path

from . import views

urlpatterns = [
    path('', views.schoolWiseEnroll, name='Enrollment')
    
]