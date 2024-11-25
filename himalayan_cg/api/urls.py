from django.urls import path
from .views import BlogListAPIView, BlogCreateAPIView, BlogUpdateAPIView

urlpatterns = [
    path('blog/', BlogListAPIView.as_view(), name='blog-list'),
    path('blog/create/', BlogCreateAPIView.as_view(), name='blog-create'),
    path('blog/<pk>/', BlogUpdateAPIView.as_view(), name='blog-update-delete'),
]