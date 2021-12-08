from django.urls import path

from . import views

urlpatterns = [
    path('Enrollment-Expand', views.schoolWiseEnrollExpand, name='Enrollment-Expand'),
    path('Enrollment-Compact', views.schoolWiseEnrollCompact, name='Enrollment-Compact')
]