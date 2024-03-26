from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('detalle/', views.detalle, name="detalle"),
    path('funcion/', views.funcion, name="funcion"),
]
