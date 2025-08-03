from django.urls import path
# from product import views
from product.api.views import LogoutUserApiView, ProductCreateAPIView, ProductListAPIView, ProductRetrieveAPIView, ProductUpdateAPIView, ProductDestroyAPIView, LoginUserApiView

urlpatterns = [
    path('products/create/', ProductCreateAPIView.as_view(), name='create_product'),
    path('products/', ProductListAPIView.as_view(), name='list_product'),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='retrieve_product'),
    path('products/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='update_product'),
    path('products/delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='delete_product'),

    # login
    path('login/', LoginUserApiView.as_view(), name='login'),
    path('logout/', LogoutUserApiView.as_view(), name='logout'),

    
    # path('products/create/', views.create_product, name='create_product'),
    # path('products/', views.get_product, name='get_product'),
    # path('products/<int:pk>/', views.get_product_detail, name='get_product_detail'),
    # path('products/edit/<int:pk>/', views.update_product, name='update_product'),
    # path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),


]