from django.shortcuts import render
from .models import Blog, FAQ, Category, Initiatives, Story, OrganizationDetail
from .serializers import OrganizationSerializer, OrganizationContactSerializer, OrganizationSocialMediaSerializer, BlogSerializer, StoriesSerializer, InitiativeSerializer, InitiativeCreateSerializer, BlogCreateSerializer, FAQSerializer, CategorySerializer
from .pagination import BlogLimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


################# Organizational Details #################
class OrganizationalDetailAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        try:
            organization = OrganizationDetail.objects.first()
        except OrganizationDetail.DoesNotExist:
            return Response(
                {'message': 'No Organization Detail Found!'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = OrganizationSerializer(organization)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, *args, **kwargs):
        organization = OrganizationDetail.objects.first()
        serializer = OrganizationSerializer(organization, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'Detail updated Successfully!',
                    'result': serializer.data
                 },
                status= status.HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationLogoUpdateView(APIView):
    permission_classes = (IsAuthenticated,)

    def patch(self, request, *args, **kwargs):
        organization = OrganizationDetail.objects.first()
        
        if not organization:
            return Response({"error": "Organization not found."}, status=status.HTTP_404_NOT_FOUND)
        
        logo = request.data.get('logo')
        
        if not logo:
            return Response({"error": "Logo file is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        organization.logo = logo
        organization.save()
        
        return Response(
            {
                'message': 'Logo Updated Successfully!',
            },
            status=status.HTTP_200_OK
        )
    

class OrganizationContactAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, rrequest, *args, **kwargs):
        try:
            organization = OrganizationDetail.objects.first()
        except OrganizationDetail.DoesNotExist:
            return Response(
                {'message': 'No Organization Detail Found!'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = OrganizationContactSerializer(organization)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, *args, **kwargs):
        contact = OrganizationDetail.objects.first()
        serializer = OrganizationContactSerializer(contact, data=request.data, partial=True)
    
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'Contact Detail updated Successfully!',
                    'result': serializer.data
                 },
                status= status.HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationSMAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, rrequest, *args, **kwargs):
        try:
            organization = OrganizationDetail.objects.first()
        except OrganizationDetail.DoesNotExist:
            return Response(
                {'message': 'No Organization Detail Found!'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = OrganizationSocialMediaSerializer(organization)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, *args, **kwargs):
        medias = OrganizationDetail.objects.first()
        serializer = OrganizationSocialMediaSerializer(medias, data=request.data, partial=True)
    
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'Social Media Detail updated Successfully!',
                    'result': serializer.data
                 },
                status= status.HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################# Blog #################
class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)
    pagination_class = BlogLimitOffsetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = ('author', 'is_featured')
    search_fields = ('author__name', 'author__email', 'title')


class BlogCreateAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateSerializer
    permission_classes = (IsAuthenticated,)


class BlogUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateSerializer
    permission_classes = (IsAuthenticated,)


class FeatureBlogAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def patch(self, request, pk, *args, **kwargs):
        # 1. Fetch the Blog Object
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response(
                {'message': "The Blog Object doesn't exist!"}
            )
        
        # 2. Check if the featured is True or False
        blog.is_featured = not blog.is_featured
        blog.save()

        # 3. if false, set to true, and vice versa
        serializer = BlogSerializer(blog)
        return Response(
            {
                'result': serializer.data,
                'message': 'Successfully updated!'
            },
            status=status.HTTP_200_OK
        )


################# FAQ #################
class FAQListCreateAPIView(ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FAQUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


################# Category #################
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoryUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


################# Initiatives #################
class InitiativeListAPIView(ListAPIView):
    queryset = Initiatives.objects.all()
    serializer_class = InitiativeSerializer
    permission_classes = (AllowAny,)
    pagination_class = BlogLimitOffsetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = ('category',)
    search_fields = ('author__name', 'author__email', 'title')


class InitiativeCreateAPIView(CreateAPIView):
    queryset = Initiatives.objects.all()
    serializer_class = InitiativeCreateSerializer
    permission_classes = (IsAuthenticated,)


class InitiativeUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Initiatives.objects.all()
    serializer_class = InitiativeCreateSerializer
    permission_classes = (IsAuthenticated,)


################# Stories #################
class StoriesListAPIView(ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StoriesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = BlogLimitOffsetPagination

    class Meta:
        ordering = ('published_at',)

class StoriesCreateAPIView(CreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StoriesSerializer
    permission_classes = (IsAuthenticated,)

class StoriesUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StoriesSerializer
    permission_classes = (IsAuthenticated,)