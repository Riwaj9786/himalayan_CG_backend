from django.urls import path
from .views import ContactListAPIView, ContactCreateAPIView

urlpatterns = [
    path('', ContactListAPIView.as_view(), name='contact-list'),
    path('create/', ContactCreateAPIView.as_view(), name='contact-create'),
]