from django.urls import path

from . import views

app_name = 'enrollment'
urlpatterns = [
    path('Enrollment-Expand', views.schoolWiseEnrollExpand, name='expanded'),
    path('Enrollment-Compact', views.schoolWiseEnrollCompact, name='compact')
]