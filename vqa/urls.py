from django.urls import path
from . import views

app_name = "vqa"

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('result/', views.result, name='result'),
]