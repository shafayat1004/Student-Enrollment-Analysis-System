from django.urls import path

from . import views

app_name = 'revenue'
urlpatterns = [
    path('', views.revenueMain, name='revenueMain'),
    path('iub', views.iubRevenue, name='iubRevenue'),
    path('sch', views.deptRevenue, name='schoolRevenue'),
]