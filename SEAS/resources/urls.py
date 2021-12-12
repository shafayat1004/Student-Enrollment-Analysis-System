from django.urls import path

from . import views

urlpatterns = [
    path('resource_usage', views.resourceUsage, name='Resource_Usage'),
    path('iub_resources', views.iubResources, name='IUB_Resources'),
    path('resource_comparison', views.resourceComp, name='Resource_Comparison')
]