from django.shortcuts import render
from rest_framework.generics import ListAPIView
from faq.models import FrequentlyAskedQuestions
from faq.serializers import FAQSerializer

# Create your views here.
class FAQListAPIView(ListAPIView):
    queryset = FrequentlyAskedQuestions.objects.all()
    serializer_class = FAQSerializer