from django.urls import path
from career.views import CareerListCreateAPIView, CareerDeleteAPIView, CareerListAllAPIView, CareerApplyListAPIView, CareerApplyCreateAPIView

urlpatterns = [
    path('', CareerListCreateAPIView.as_view(), name='career-list'),
    path('all/', CareerListAllAPIView.as_view(), name='career-all'),
    path('apply/<int:pk>/', CareerApplyCreateAPIView.as_view(), name='career-apply'),
    path('applied/', CareerApplyListAPIView.as_view(), name='applied_careers'),
    path('delete/<pk>/', CareerDeleteAPIView.as_view(), name='career-delete'),
]