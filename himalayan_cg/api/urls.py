from django.urls import path
from .views import (
                        BlogListAPIView, 
                        BlogCreateAPIView, 
                        FeatureBlogAPIView, 
                        BlogUpdateAPIView, 
                        CategoryUpdateAPIView, 
                        FAQUpdateAPIView, 
                        FAQListCreateAPIView, 
                        CategoryListCreateAPIView,
                        InitiativeListAPIView,
                        InitiativeCreateAPIView,
                        InitiativeUpdateAPIView,
                        StoriesListAPIView,
                        StoriesCreateAPIView,
                        StoriesUpdateAPIView,
                        OrganizationalDetailAPIView,
                        OrganizationLogoUpdateView,
                        OrganizationContactAPIView,
                        OrganizationSMAPIView,
                    )


urlpatterns = [
    # Blog
    path('blog/', BlogListAPIView.as_view(), name='blog-list'),
    path('blog/create/', BlogCreateAPIView.as_view(), name='blog-create'),
    path('blog/<pk>/', BlogUpdateAPIView.as_view(), name='blog-update-delete'),
    path('blog/<pk>/feature/', FeatureBlogAPIView.as_view(), name='feature-blog'),
    
    #FAQ
    path('faq/', FAQListCreateAPIView.as_view(), name='faqs'),
    path('faq/<pk>/', FAQUpdateAPIView.as_view(), name='faqs-update-delete'),
    
    #Category
    path('category/', CategoryListCreateAPIView.as_view(), name='category'),
    path('category/<pk>/', CategoryUpdateAPIView.as_view(), name='category-update-delete'),
    
    # Initiatives
    path('initiatives/', InitiativeListAPIView.as_view(), name='initiatives-list'),
    path('initiatives/create/', InitiativeCreateAPIView.as_view(), name='initiatives-create'),
    path('initiatives/<pk>/', InitiativeUpdateAPIView.as_view(), name='initiatives-update-delete'),
    
    # Story
    path('stories/', StoriesListAPIView.as_view(), name='stories-list'),
    path('stories/create/', StoriesCreateAPIView.as_view(), name='stories-create'),
    path('stories/<pk>/', StoriesUpdateAPIView.as_view(), name='stories-update-delete'),

    # Organization Detail
    path('info/', OrganizationalDetailAPIView.as_view(), name='organization-detail'),
    path('info/update-logo/', OrganizationLogoUpdateView.as_view(), name='logo_update'),
    path('info/contact/', OrganizationContactAPIView.as_view(), name='contact-detail'),
    path('info/media/', OrganizationSMAPIView.as_view(), name="social-media-info"),
]