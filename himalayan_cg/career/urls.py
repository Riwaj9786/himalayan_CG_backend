from django.urls import path
from career.views import CareerListAPIView, CareerDetailAPIView, CareerApplyCreateAPIView

urlpatterns = [
    path('openings/', CareerListAPIView.as_view(), name='career-list'),
    path('<str:uuid>/', CareerDetailAPIView.as_view(), name='career-detail'),
    path('apply/<str:uuid>/', CareerApplyCreateAPIView.as_view(), name='career-apply'),
]