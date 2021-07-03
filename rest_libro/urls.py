from django.urls import path
from rest_libro.views import detalle_libro, lista_libros
from rest_libro import views
from rest_libro.viewslogin import login

urlpatterns = [
    path('lista_libros', lista_libros, name="lista_libros"),
    path('detalle_libro/<id>', detalle_libro, name="detalle_libro"),
    path('login', login, name="login"),
]