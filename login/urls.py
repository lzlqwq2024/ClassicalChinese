from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('index/<slug:name>/', views.index),
    path('upload_image/', views.upload_image),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('reset/', views.reset),
    path('confirm/', views.user_confirm),
    path('resetpassword/', views.resetpassword),
]