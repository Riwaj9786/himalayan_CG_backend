from django.urls import path
from .views import ProposalListAPIView, ProposalCreateAPIView

urlpatterns = [
    path('', ProposalListAPIView.as_view(), name='proposal-list'),
    path('apply/', ProposalCreateAPIView.as_view(), name='proposal-create'),
]