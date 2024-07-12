from django.urls import path
from .views import ProductListCreateView, ProductDetailView, UpdateProductQuantityView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:pk>/update-quantity/', UpdateProductQuantityView.as_view(), name='update-product-quantity'),
]
