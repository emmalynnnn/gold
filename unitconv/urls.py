from django.urls import path

from . import views

urlpatterns = [
    path('convert/', views.index, name='index'),
]