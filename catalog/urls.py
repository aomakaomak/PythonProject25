from django.urls import path

from . import views

from .views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, ProductDeleteView, IsPublishedProductView

app_name = 'catalog'

urlpatterns = [
    path('home/', ProductListView.as_view(), name='home'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('new/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('is_publishes/<int:pk>/', IsPublishedProductView.as_view(), name='product_is_published'),


    # path('home/', views.home, name='home'),
    # path('contacts/', views.contacts, name='contacts'),
    # path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
]