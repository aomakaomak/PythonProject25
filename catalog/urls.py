from django.urls import path

from . import views

from .views import ProductListView, ProductDetailView, ContactsView

app_name = 'catalog'

urlpatterns = [
    path('home/', ProductListView.as_view(), name='home'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),


    # path('home/', views.home, name='home'),
    # path('contacts/', views.contacts, name='contacts'),
    # path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
]