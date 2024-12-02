from blog.models import Blog, FeaturedBlog, Initiatives, FeaturedInitiatives
from blog.serializers import BlogListSerializer, BlogDetailSerializer, FeatureBlogSerializer, InitiativeListSerializer, InitiativeDetailSerializer, FeaturedInitiativeSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Create your views here.
class BlogListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer

class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer

class FeaturedBlogListView(ListAPIView):
    queryset = FeaturedBlog.objects.all()
    serializer_class = FeatureBlogSerializer

class InitiativesListView(ListAPIView):
    queryset = Initiatives.objects.all()
    serializer_class = InitiativeListSerializer
    
class InitiativesDetailView(RetrieveAPIView):
    queryset = Initiatives.objects.all()
    serializer_class = InitiativeDetailSerializer

class FeaturedInitiativesListView(ListAPIView):
    queryset = FeaturedInitiatives.objects.all()
    serializer_class = FeaturedInitiativeSerializer