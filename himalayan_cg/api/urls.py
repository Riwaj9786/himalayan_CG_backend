from django.urls import path
from .views import BlogListAPIView, BlogCreateAPIView, BlogUpdateAPIView, CategoryUpdateAPIView, FAQUpdateAPIView, FAQListCreateAPIView, CategoryListCreateAPIView

urlpatterns = [
    path('blog/', BlogListAPIView.as_view(), name='blog-list'),
    path('blog/create/', BlogCreateAPIView.as_view(), name='blog-create'),
    path('blog/<pk>/', BlogUpdateAPIView.as_view(), name='blog-update-delete'),
    path('faq/', FAQListCreateAPIView.as_view(), name='faqs'),
    path('faq/<pk>/', FAQUpdateAPIView.as_view(), name='faqs-update-delete'),
    path('category/', CategoryListCreateAPIView.as_view(), name='category'),
    path('category/<pk>/', CategoryUpdateAPIView.as_view(), name='category-update-delete'),
    # Initiatives
    # Organization Detail
]