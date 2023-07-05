from django.urls import path, include
from cartelera import views

urlpatterns = [
    path('', views.index, name='index'),
]
