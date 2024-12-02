from django.urls import path
from career.views import CareerListAPIView, CareerDetailAPIView, CareerApplyCreateAPIView

urlpatterns = [
    path('openings/', CareerListAPIView.as_view(), name='career-list'),
    path('openings/<str:pk>/', CareerDetailAPIView.as_view(), name='career-detail'),
    path('apply/<str:pk>/', CareerApplyCreateAPIView.as_view(), name='career-apply'),
]