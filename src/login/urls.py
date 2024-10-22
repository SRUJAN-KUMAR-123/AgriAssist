from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index_page, name="home"),
    path('select-user', views.selectUser_page, name="selectuser"),
    path('farmer-registration', views.farmerRegistration, name="farmerregistration"),
    path('user-registration', views.userRegistration, name="user-registration"),
    path('register', views.createUser, name="register"),
    path('login', views.login_page, name="login"),
    path('logout', views.userLogout, name="logout"),
    path('loginvalidation', views.login_validation, name="loginvalidate"),
    path('dashboard', views.dashboard, name="dashboard")
    
    
    
    # path('admin/', admin.site.urls),
]
