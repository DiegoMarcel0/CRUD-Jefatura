from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path( "empleado/", views.empleadoView.as_view(), name="empleado"),
    
    path( "empleado/<int:pk>", views.empleadoDetallesView.as_view(), name="detalles"),
    #Formularios De Creacion
    path( "empleado/crear", views.empleado_form, name="empleado_crear"),
    path( "oficial/", views.oficial_form, name="oficial"),
    path( "caso/", views.caso_form, name="caso"),
    #path( "reporte/servicio", views.empleado_form, name="empleado"),
    #path( "reporte/<int:caso>", views.oficial_form, name="oficial"),
    #Login//logout
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    #Index
    path( "inicio/", views.index, name="inicio"),
]