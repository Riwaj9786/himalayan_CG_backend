from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from career.models import Career, CareerApply
from career.serializers import CareerSerializer, CareerApplySerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import ValidationError

# Create your views here.
class CareerListCreateAPIView(ListCreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('position_type', 'job_type', 'job_location')

    def list(self, request, *args, **kwargs):
        queryset = Career.objects.filter(_is_active=True, deadline__gte=timezone.now())
        filter_queryset = self.filter_queryset(queryset)

        serializer = CareerSerializer(filter_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CareerListAllAPIView(ListAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (DjangoFilterBackend, SearchFilter )
    filterset_fields = ('position_type', 'job_type', 'job_location', '_is_active')
    search_fields = ('position_name',)


class CareerApplyCreateAPIView(CreateAPIView):
    queryset = CareerApply.objects.all()
    serializer_class = CareerApplySerializer

    def perform_create(self, serializer):
        # Extract position ID from the URL parameter 'pk'
        position_id = self.kwargs['pk']
        
        try:
            position = Career.objects.get(id=position_id)
        except Career.DoesNotExist:
            raise ValidationError({'error': 'The career position does not exist!'})

        # Check if the position is still active
        if not position.is_active:
            raise ValidationError({'error': 'The Position you are applying for is not active anymore!'})

        # Save the application if the position is active
        serializer.save(position=position)
        

class CareerApplyListAPIView(ListAPIView):
    queryset = CareerApply.objects.all()
    serializer_class = CareerApplySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = ('position', 'position__position_type')
    search_fields = ('position__position_name',)


class CareerDeleteAPIView(DestroyAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = (IsAdminUser,)