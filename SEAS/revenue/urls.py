from django.urls import path

from . import views

urlpatterns = [
    path('', views.iubRevenue, name='Revenue of IUB'),
]