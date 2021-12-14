from django.urls import path

from . import views
app_name = 'resources'
urlpatterns = [
    path('resource_usage', views.resourceUsage, name='Resource_Usage'),
    path('resource_comparison', views.resourceComp, name='Resource_Comparison')
]