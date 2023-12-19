from . import views
from django.urls import path

urlpatterns = [
    
    path('Dashboard/', views.dashboard , name = "Dashboard"),
    path('logout/', views.logout_user, name='Logout'),
    path('Update/', views.update, name='Update'),
    path('GET/<str:Type>/<str:ID>',views.get,name='GET'),
    path('',views.login_page,name="Login"),
]
