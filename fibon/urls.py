from django.urls import path
from .import views

urlpatterns = [
    path('', views.fibonacci, name='fibonacci'),
    path('index', views.index, name='index'),
]
