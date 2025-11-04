from django.urls import path

from . import views

from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

app_name = 'blog'

urlpatterns = [
    path('blog/', BlogPostListView.as_view(), name='blog'),
    path('blogpost_detail/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('blog/new/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('blog/update/<int:pk>/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('books/delete/<int:pk>/', BlogPostDeleteView.as_view(), name='blogpost_delete'),

    # path('contacts/', ContactsView.as_view(), name='contacts'),


    # path('home/', views.home, name='home'),
    # path('contacts/', views.contacts, name='contacts'),
    # path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
]