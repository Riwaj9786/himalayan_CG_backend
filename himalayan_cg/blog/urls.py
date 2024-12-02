from django.urls import path
from blog.views import (
    BlogListView,
    BlogDetailView,
    FeaturedBlogListView,
    InitiativesListView,
    InitiativesDetailView,
    FeaturedInitiativesListView
)

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('<str:uuid>/', BlogDetailView.as_view(), name='blog-detail'),
    path('featured/', FeaturedBlogListView.as_view(), name='featured-blogs'),
    path('initiatives/', InitiativesListView.as_view(), name='blog-list'),
    path('initiatives/<str:uuid>/', InitiativesDetailView.as_view(), name='blog-detail'),
    path('featured/', FeaturedInitiativesListView.as_view(), name='featured-blogs'),
]