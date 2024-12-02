from rest_framework.generics import ListAPIView, RetrieveAPIView
from UserProfile.serializers import ProfileSerializer, TeamSerializer, MemberSerializer
from UserProfile.models import Profile, Team
from rest_framework.filters import SearchFilter 

# Create your views here.
class BoardOfDirectorsListAPIView(ListAPIView):
    queryset = Profile.objects.exclude(position__isnull=True)
    serializer_class = MemberSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'position')


class TeamListAPIView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('team_name',)


class ProfileDetailView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# class ProfileAPIView(APIView):
#     permission_classes = (IsAdminUser,)

#     def get(self, request, pk=None, *args, **kwargs):
#         if pk:
#             try:
#                 queryset = Profile.objects.get(pk=pk)
#                 serializer = ProfileSerializer(queryset)

#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except Profile.DoesNotExist:
#                 return Response(
#                     {'message': 'Profile does not Exists!'},
#                     status=status.HTTP_404_NOT_FOUND
#                 )
#         else:
#             queryset = Profile.objects.all()
#             serializer = ProfileSerializer(queryset, many=True)

#             return Response(serializer.data, status=status.HTTP_200_OK)
    

#     def post(self, request, *args, **kwargs):
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {
#                     'message': 'Profile Created Successfully!',
#                     'data': serializer.data
#                  },
#                  status=status.HTTP_201_CREATED
#             )
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def patch(self, request, pk, *args, **kwargs):
#         try:
#             profile = Profile.objects.get(pk=pk)
#         except Profile.DoesNotExist:
#             return Response(
#                 {'message': 'Profile is not Found!'},
#                 status=status.HTTP_404_NOT_FOUND
#             ) 
        
#         serializer = ProfileSerializer(profile, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {
#                     'message': 'Profile updated successfully!',
#                     'data': serializer.data
#                 },
#                 status=status.HTTP_200_OK
#             )
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def delete(self, request, pk, *args, **kwargs):
    #     try:
    #         profile = Profile.objects.get(pk=pk)
    #     except Profile.DoesNotExist:
    #         return Response(
    #             {'message': 'Profile is not Found!'},
    #             status=status.HTTP_404_NOT_FOUND
    #         )      
        
    #     profile.delete()
    #     return Response(
    #         {'message': 'Profile Deleted Successfully!'},
    #         status= status.HTTP_204_NO_CONTENT
    #     )
    
    
# class UpdateProfileAPIView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def patch(self, request, pk, *args, **kwargs):
#         try:
#             profile = Profile.objects.get(pk=pk)
#         except Profile.DoesNotExist:
#             return Response(
#                 {'message': 'Profile does not Exist!'},
#                 status = status.HTTP_404_NOT_FOUND
#             )
        
#         image = request.FILES.get('image')
#         if image:
#             profile.image = image
#             profile.save()
#             return Response(
#                 {
#                     'message': 'Profile Image Updated Successfully!',
#                 },
#                 status= status.HTTP_200_OK
#             )
#         else:
#             return Response(
#                 {'message': 'No Image provided to update!'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        

# class TeamAPIView(ListCreateAPIView):
#     queryset = Team.objects.all()
#     serializer_class = TeamSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     filter_backends = (SearchFilter,)
#     search_fields = ('team_name',)


# class TeamRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Team.objects.all()
#     serializer_class = TeamSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
