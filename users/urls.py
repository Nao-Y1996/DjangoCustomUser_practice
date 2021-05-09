from django.contrib import admin
from django.urls import path, include
from . import views

app_name="users"
urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path('logout',  views.Logout.as_view(), name='logout'),
    path('index', views.top, name='top'),
    
    path('user_create/', views.UserCreate.as_view(), name='user_create'),
    path('user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
    path('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),


]
