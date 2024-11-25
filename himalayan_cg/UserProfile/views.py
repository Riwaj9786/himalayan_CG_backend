from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from UserProfile.serializers import ProfileSerializer, TeamSerializer, BoardOfDirectorSerializer
from UserProfile.models import Profile, Team, BoardOfDirectors
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter 

# Create your views here.
class ProfileAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                queryset = Profile.objects.get(pk=pk)
                serializer = ProfileSerializer(queryset)

                return Response(serializer.data, status=status.HTTP_200_OK)
            except Profile.DoesNotExist:
                return Response(
                    {'message': 'Profile does not Exists!'},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            queryset = Profile.objects.all()
            serializer = ProfileSerializer(queryset, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request, *args, **kwargs):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'Profile Created Successfully!',
                    'data': serializer.data
                 },
                 status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, pk, *args, **kwargs):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response(
                {'message': 'Profile is not Found!'},
                status=status.HTTP_404_NOT_FOUND
            ) 
        
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'Profile updated successfully!',
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, *args, **kwargs):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response(
                {'message': 'Profile is not Found!'},
                status=status.HTTP_404_NOT_FOUND
            )      
        
        profile.delete()
        return Response(
            {'message': 'Profile Deleted Successfully!'},
            status= status.HTTP_204_NO_CONTENT
        )
    
    
class UpdateProfileAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def patch(self, request, pk, *args, **kwargs):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response(
                {'message': 'Profile does not Exist!'},
                status = status.HTTP_404_NOT_FOUND
            )
        
        image = request.FILES.get('image')
        if image:
            profile.image = image
            profile.save()
            return Response(
                {
                    'message': 'Profile Image Updated Successfully!',
                },
                status= status.HTTP_200_OK
            )
        else:
            return Response(
                {'message': 'No Image provided to update!'},
                status=status.HTTP_400_BAD_REQUEST
            )
        

class TeamAPIView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ('team_name',)


class TeamRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class BoardOfDirectorsListCreateAPIView(ListCreateAPIView):
    queryset = BoardOfDirectors.objects.all()
    serializer_class = BoardOfDirectorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('position', )
    search_fields = ('name', 'position', 'phone')


class BoardofDirectorsUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BoardOfDirectors.objects.all()
    serializer_class = BoardOfDirectorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)