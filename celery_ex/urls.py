from django.urls import path

from celery_ex import views


app_name = 'celery_ex'

urlpatterns = [
    path('', views.home, name='home'),
    path('celery_ex/', views.celery_ex, name='celery_ex'),
    path('error/', views.error, name='error'),
]