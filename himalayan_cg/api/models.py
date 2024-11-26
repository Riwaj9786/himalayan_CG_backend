import os
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 

# Create your models here.
########## Blog/News ############
# 1. is_featured
# 2. title
# 3. published_at
# 4. author
# 5. feature image
# 6. BaseModel: Introduction, Content, Conclusion

def image_upload_file(instance, filename):
    title = instance.title

    return os.path.join('featured_images/', f"{title}_{filename}")


class BaseBlogModel(models.Model):
    title = models.CharField(
        max_length=60
    )
    introduction = RichTextUploadingField()
    content = RichTextUploadingField()
    conclusion = RichTextUploadingField()
    published_at = models.DateTimeField(auto_now_add=True)
    feature_image = models.ImageField(upload_to=image_upload_file, null=True, blank=True)

    class Meta:
        abstract = True

    
class Category(models.Model):
    category_name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class Blog(BaseBlogModel):
    author = models.ForeignKey('UserProfile.Profile', on_delete=models.DO_NOTHING, related_name='blog_author')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='blog_category', null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"


########## OrganizationInformation ############
# 1. Tagline
# 2. email
# 3. phone
# 4. office 
# 5. Social Media Links
# 6. Mission
# 7. Vision

class OrganizationDetail(models.Model):
    name = models.CharField(max_length=155)
    tagline = models.TextField(null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    logo = models.FileField(upload_to='organization/logo/', null=True, blank=True)
    location = models.TextField()
    facebook = models.URLField(null=True, blank=True)      
    instagram = models.URLField(null=True, blank=True)      
    twitter = models.URLField(null=True, blank=True)      
    linkedin = models.URLField(null=True, blank=True)

    mission = models.TextField()
    vision = models.TextField()

    def __str__(self):
        return self.name

# Initiatives
class Initiatives(BaseBlogModel):
    description = RichTextUploadingField(blank=True)
    author = models.ForeignKey('UserProfile.Profile', on_delete=models.DO_NOTHING, related_name='initiative_author', null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='initiative_category', null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Initiative'
        verbose_name_plural = 'Initiatives'

# Stories
class Story(BaseBlogModel):
    sub_title = models.CharField(max_length=255)
    created_by = models.ForeignKey('UserProfile.Profile', on_delete=models.DO_NOTHING, related_name='story_author', null=True)

    class Meta:
        verbose_name_plural = "Stories"


# FAQs
class FAQ(models.Model):
    question = RichTextUploadingField()
    answer = RichTextUploadingField()

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return f"{self.id}-{self.question}"