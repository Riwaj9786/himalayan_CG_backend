from django.db import models
from django.core.validators import MinValueValidator
from ckeditor_uploader.fields import RichTextUploadingField 
import uuid


class BaseBlogModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(
        max_length=60
    )
    short_description = models.CharField(max_length=255)
    
    introduction = RichTextUploadingField()
    content = RichTextUploadingField()
    conclusion = RichTextUploadingField()
    
    read_time = models.IntegerField(validators=[MinValueValidator(1)], blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    
class BlogCategory(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "5. Blog Categories"

    def __str__(self):
        return self.name
    
    
class InitiativeCategory(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Initiative Category"
        verbose_name_plural = "6. Initiative Categories"

    def __str__(self):
        return self.name
    


class Blog(BaseBlogModel):
    category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT, related_name='blog_category')
    author = models.ForeignKey('UserProfile.Profile', on_delete=models.PROTECT, related_name='blog_author')

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "1. Blogs"

    def __str__(self):
        return f"{self.title}"


class FeaturedBlog(models.Model):
    featured_blog_1 = models.ForeignKey(Blog, on_delete=models.PROTECT, related_name='feature_blog_1', blank=True)
    featured_blog_2 = models.ForeignKey(Blog, on_delete=models.PROTECT, related_name='feature_blog_2', blank=True)
    featured_blog_3 = models.ForeignKey(Blog, on_delete=models.PROTECT, related_name='feature_blog_3', blank=True)
    featured_blog_4 = models.ForeignKey(Blog, on_delete=models.PROTECT, related_name='feature_blog_4', blank=True)

    class Meta:
        verbose_name = 'Featured Blog'
        verbose_name_plural = '3. Featured Blogs'

    def __str__(self):
        return "Featured Blogs!"
    


# Initiatives
class Initiatives(BaseBlogModel):
    category = models.ForeignKey(InitiativeCategory, on_delete=models.PROTECT, related_name='initiative_category', null=True)
    author = models.ForeignKey('UserProfile.Profile', on_delete=models.PROTECT, related_name='initiative_author')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Initiative'
        verbose_name_plural = '2. Initiatives'


class FeaturedInitiatives(models.Model):
    featured_initiative_1 = models.ForeignKey(Initiatives, on_delete=models.PROTECT, related_name='featured_initiative_1')
    featured_initiative_2 = models.ForeignKey(Initiatives, on_delete=models.PROTECT, related_name='featured_initiative_2')
    featured_initiative_3 = models.ForeignKey(Initiatives, on_delete=models.PROTECT, related_name='featured_initiative_3')
    featured_initiative_4 = models.ForeignKey(Initiatives, on_delete=models.PROTECT, related_name='featured_initiative_4')

    class Meta:
        verbose_name = 'Featured Initiative'
        verbose_name_plural = "4. Featured Initiatives"