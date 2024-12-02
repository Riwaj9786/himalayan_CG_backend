from django.contrib import admin
from blog.models import Blog, BlogCategory, FeaturedBlog, FeaturedInitiatives, InitiativeCategory, Initiatives

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description',)
    list_display_links = ('title', 'short_description',)
    readonly_fields = ('created_at', 'updated_at',)

@admin.register(Initiatives)
class InitiativesAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description',)
    list_display_links = ('title', 'short_description',)
    readonly_fields = ('created_at', 'updated_at',)

admin.site.register(FeaturedInitiatives)
admin.site.register(FeaturedBlog)
admin.site.register(BlogCategory)
admin.site.register(InitiativeCategory)