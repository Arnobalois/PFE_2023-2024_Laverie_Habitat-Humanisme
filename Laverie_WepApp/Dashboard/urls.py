from . import views
from django.urls import path

urlpatterns = [
    
    path('Dashboard/', views.dashboard , name = "Dashboard"),
    path('logout/', views.logout_user, name='Logout'),
    path('Update/', views.update, name='Update'),
    path('begin/',views.start,name="Start"),
    path('',views.login_page,name="Login"),
]
