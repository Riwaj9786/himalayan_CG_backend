from django.contrib import admin
from UserProfile.models import Profile, Team
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
            'classes': ('collapse',),
        }),
        ('Social Media Handles', {
            'fields': ('facebook', 'instagram', 'twitter'),
            'classes': ('collapse',),
        }),
    )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name',)
    fieldsets = (
        ('Team Name', {'fields': ('team_name',)}),
        ('Description', {'fields': ('description',)})
    )