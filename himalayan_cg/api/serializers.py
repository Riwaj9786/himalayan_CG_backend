from rest_framework import serializers
from .models import Blog, FAQ, Initiatives, Category, Story, OrganizationDetail
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


# Stories
class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'title', 'sub_title', 'introduction', 'content', 'conclusion', 'published_at', 'feature_image')
        read_only_fields = ('id', 'published_at',)

# Organizational Detail
class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDetail
        fields = ('name', 'tagline', 'logo', 'mission', 'vision')

class OrganizationContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDetail
        fields = ('email', 'phone', 'location',)

class OrganizationSocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDetail
        fields = ('facebook', 'instagram', 'twitter', 'linkedin')

# Blog and News
class BlogSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ('id', 'title', 'author', 'introduction', 'content', 'conclusion', 'published_at', 'is_featured', 'feature_image')
        read_only_fields = ('id', 'author')


class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'author', 'introduction', 'content', 'conclusion', 'published_at', 'is_featured', 'feature_image')
        read_only_fields = ('id',)

#FAQs
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', 'question', 'answer',)
        read_only_fields = ('id',)