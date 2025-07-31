from django.urls import path
from product import views

urlpatterns = [
    path('products/create/', views.create_product, name='create_product'),
    path('products/', views.get_product, name='get_product'),
    path('products/<int:pk>/', views.get_product_detail, name='get_product_detail'),
    path('products/edit/<int:pk>/', views.update_product, name='update_product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),
]