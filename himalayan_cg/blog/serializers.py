from rest_framework import serializers
from blog.models import (
    Blog,
    Initiatives,
    BlogCategory,
    InitiativeCategory,
    FeaturedBlog,
    FeaturedInitiatives,
)

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ('name',)


class BlogListSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ('uuid', 'title', 'short_description', 'read_time', 'author', 'category__name')
        read_only_fields = ('uuid', 'category__name')


class BlogDetailSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ('uuid', 'title', 'introduction', 'content', 'conclusion', 'read_time', 'category__name', 'created_at', 'updated_at')
        read_only_fields = ('uuid', 'category__name')


class InitiativeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InitiativeCategory
        fields = ('name',)


class InitiativeListSerializer(serializers.ModelSerializer):
    category = InitiativeCategorySerializer(read_only=True)
    class Meta:
        model = Initiatives
        fields = ('uuid', 'title', 'short_description', 'read_time', 'author', 'category__name')
        read_only_fields = ('uuid', 'category__name')


class InitiativeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Initiatives
        fields = ('uuid', 'title', 'introduction', 'content', 'conclusion', 'read_time', 'author', 'created_at', 'updated_at')
        read_only_fields = ('uuid', 'category__name')


class FeatureBlogSerializer(serializers.ModelSerializer):
    blog1 = BlogListSerializer(read_only=True)
    blog2 = BlogListSerializer(read_only=True)
    blog3 = BlogListSerializer(read_only=True)
    blog4 = BlogListSerializer(read_only=True)
    
    class Meta:
        model = FeaturedBlog
        fields = ('blog1', 'blog2', 'blog3', 'blog4',)


class FeaturedInitiativeSerializer(serializers.ModelSerializer):
    initiative1 = InitiativeListSerializer(read_only=True)
    initiative2 = InitiativeListSerializer(read_only=True)
    initiative3 = InitiativeListSerializer(read_only=True)
    initiative4 = InitiativeListSerializer(read_only=True)

    class Meta:
        model = FeaturedInitiatives
        fields = ('initiative1', 'initiative2', 'initiative3', 'initiative4')