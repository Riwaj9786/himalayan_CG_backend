from django.contrib import admin
from api.models import Blog, Story, Initiatives, OrganizationDetail, FAQ

# Register your models here.
@admin.register(OrganizationDetail)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline')
    list_display_links = ('name', 'tagline')

    fieldsets = (
        ("Information", {
            "fields": ("name", "tagline", "email", "phone", "location"),
        }),
        ("Logo", {
            "fields": ("logo",),
        }),
        ("Social Media", {
            "fields": ("facebook", "instagram", "twitter", "linkedin"),
        }),
        ("Mission/Vision", {
            "fields": ("mission", "vision"),
        }),
    )

admin.site.register(Blog)
admin.site.register(Initiatives)
admin.site.register(FAQ)

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title')
    list_display_links = ('title', 'sub_title')