from django.urls import path

from . import views

app_name = 'products' 
urlpatterns = [
    path('', views.index, name='index'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('deleteProduct/<int:id>/', views.deleteProduct, name='deleteProduct'),
    path('getProduct/<int:id>/', views.getProduct, name='getProduct'),
    path('updateProduct/<int:id>/', views.updateProduct, name='updateProduct')
]