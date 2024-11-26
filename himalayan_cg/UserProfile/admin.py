from django.contrib import admin
from UserProfile.models import Profile, BoardOfDirectors, Team
from django.utils.html import format_html

# Register your models here.
@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_display_links = ('name', 'email')
    search_fields = ('name', 'email',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'image', 'email', 'phone', 'team',),
        }),
        ('Social Media Handles', {
            'fields': ('facebook', 'instagram', 'twitter'),
            'classes': ('collapse',),
        }),
    )

@admin.register(BoardOfDirectors)
class BoardOfDirectorsAdmin(admin.ModelAdmin):
    list_display = ('name','display_image', 'position', 'email', )
    list_display_links = ('name', 'position', 'email',)
    search_fields = ('name', 'email', 'position')

    fieldsets = (
        ('Basic information', {
            'fields': ('name', 'image', 'email', 'phone', 'position', 'rank'),
        }),
        ('Social Media Handles', {
            'fields': ('facebook', 'instagram', 'twitter'),
            'classes': ('collapse',),
        })
    )

    def display_image(self, obj):
        """Display profile picture as a thumbnail in the admin list."""
        if obj.image:
            return format_html('<img src="{}" style="border-radius: 50%; width: 40px; height: 40px;" />', obj.image.url)
        return "No image"
    
    display_image.short_description = ''

admin.site.register(Team)
