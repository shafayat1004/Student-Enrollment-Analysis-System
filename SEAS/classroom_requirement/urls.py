from django.urls import path

from . import views
app_name = 'classroom_requirement'
urlpatterns = [
    path('', views.classReq, name='classReq'),
]