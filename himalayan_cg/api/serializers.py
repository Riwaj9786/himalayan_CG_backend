from rest_framework import serializers
from .models import Blog
from UserProfile.serializers import ProfileSerializer

# Initiatives
# Organizational Detail


# Blog and News
class BlogSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ('id', 'title', 'author', 'introduction', 'content', 'conclusion', 'published_at', 'feature_image')
        read_only_fields = ('id', 'author')


class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'author', 'introduction', 'content', 'conclusion', 'published_at', 'feature_image')
        read_only_fields = ('id',)

#FAQs