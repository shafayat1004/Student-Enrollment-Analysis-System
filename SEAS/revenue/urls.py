from django.urls import path

from . import views

urlpatterns = [
    path('', views.revenueMain, name='Revenue'),
    path('iub', views.iubRevenue, name='Revenue of IUB'),
    path('sch', views.deptRevenue, name='Revenue of School'),
]