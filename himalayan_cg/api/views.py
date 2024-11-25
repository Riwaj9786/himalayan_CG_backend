from django.shortcuts import render
from .models import Blog, FAQ, Category
from .serializers import BlogSerializer, BlogCreateSerializer, FAQSerializer, CategorySerializer
from .pagination import BlogLimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.
class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)
    pagination_class = BlogLimitOffsetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = ('author',)
    search_fields = ('author__name', 'author__email', 'title')


class BlogCreateAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateSerializer
    permission_classes = (IsAuthenticated,)


class BlogUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateSerializer
    permission_classes = (IsAuthenticated,)


class FAQListCreateAPIView(ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FAQUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoryUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)