from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from career.models import Career, CareerApply
from career.serializers import CareerListSerializer, CareerApplySerializer, CareerDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import ValidationError

# Create your views here.
class CareerListAPIView(ListAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('position_type', 'job_type', 'job_location')
    search_fields = ('position_name',) 

    def list(self, request, *args, **kwargs):
        try:
            queryset = Career.objects.filter(_is_active=True, opening_date__lte=timezone.now(), deadline__gte=timezone.now())
            filter_queryset = self.filter_queryset(queryset)
        except:
            return Response(
                {'message': 'No Current Openings!'},
                status=status.HTTP_204_NO_CONTENT
            )
        
        serializer = CareerListSerializer(filter_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CareerDetailAPIView(RetrieveAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerDetailSerializer
    

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
        