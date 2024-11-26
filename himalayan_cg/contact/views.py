from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Contact
from .serializers import ContactSerializers

# Create your views here.
class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    permission_classes = (IsAdminUser,)


class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    permission_classes = (AllowAny,)