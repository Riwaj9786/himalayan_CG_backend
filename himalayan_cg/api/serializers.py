from rest_framework import serializers
from .models import Blog, FAQ, Initiatives, Category
from UserProfile.serializers import ProfileSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name',)
        read_only_fields = ('id',)


# Initiatives
class InitiativeSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Initiatives
        fields = ('id', 'title', 'introduction', 'content', 'conclusion', 'published_at', 'feature_image', 'description', 'author', 'category')
        read_only_fields = ('id', 'category', 'author')


class InitiativeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Initiatives
        fields = ('id', 'title', 'introduction', 'content', 'conclusion', 'published_at', 'feature_image', 'description', 'author', 'category')
        read_only_fields = ('id',)


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
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', 'question', 'answer',)
        read_only_fields = ('id',)