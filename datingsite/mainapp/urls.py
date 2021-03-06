from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('checkuser/', views.checkuser, name='checkuser'),
    path('messages/', views.messages, name='messages'),
]
