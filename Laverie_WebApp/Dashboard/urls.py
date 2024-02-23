from . import views
from django.urls import path

urlpatterns = [
    
    path('Accueil', views.Accueil , name = "Accueil"),
    path('Logout', views.logout_user, name='Logout'),
    path('Update/', views.update, name='Update'),
    path('Begin/',views.start,name="Start"),
    path('Administration',views.Admin,name="Administration"),
    path('Convert',views.Convert,name="Conversion"),
    path('Login',views.login_page,name="Login"),
    path('',views.login_page,name="Root")
]
