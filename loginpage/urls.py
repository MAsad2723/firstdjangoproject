from django.contrib import admin
from django.urls import path
from loginpage import views
urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.loginUser, name='login'),
    path('signup', views.signupUser, name='signup'),
    path('logout', views.logoutUser, name='logout'),
]