from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #Listas en general
    path( "empleado/", views.EmpleadoView.as_view(), name="empleado"),
    path( "oficial/", views.OficialView.as_view(), name="oficial"),
    path( "caso/", views.CasoView.as_view(), name="caso"),
    #Formularios De Creacion
    path( "empleado/crear", views.empleado_form, name="empleado_crear"),
    path( "oficial/crear", views.oficial_form, name="oficial_crear"),
    path( "caso/crear", views.caso_form, name="caso_crear"),
    #Detalles de un campo
    path( "empleado/<int:pk>", views.EmpleadoDetallesView.as_view(), name="empleado_deta"),
    path( "oficial/<int:pk>", views.OficialDetallesView.as_view(), name="oficial_deta"),
    path( "caso/<int:pk>", views.CasoDetallesView.as_view(), name="caso_deta"),
    #path( "reporte/servicio", views.empleado_form, name="empleado"),
    #path( "reporte/<int:caso>", views.oficial_form, name="oficial"),
    #Editar campo
    path( "empleado/edit/<int:pk>", views.EmpleadoUpdate.as_view(), name="empleado_edit"),
    path( "oficial/edit/<int:pk>", views.OficialUpdate.as_view(), name="oficial_edit"),
    path( "caso/edit/<int:pk>", views.CasoUpdate.as_view(), name="caso_edit"),
    #Login//logout
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    #Index
    path( "inicio/", views.index, name="inicio"),
]