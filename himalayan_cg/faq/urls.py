from django.urls import path
from faq.views import FAQListAPIView

urlpatterns = [
    path('', FAQListAPIView.as_view(), name='faq'),
]