from . import views
from django.urls import path

urlpatterns = [
    
    path('Dashboard/', views.dashboard , name = "Dashboard"),
    path('logout/', views.logout_user, name='Logout'),
    path('',views.login_page,name="Login"),
]
