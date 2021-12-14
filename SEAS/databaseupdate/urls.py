from django.urls import path

from . import views
app_name = 'databaseupdate'
urlpatterns = [
    path('', views.upload_file, name='upload_file'),
]