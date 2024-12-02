from django.contrib import admin
from .models import OrganizationDetail, Goal, ImportantGoals, WhatIsHCG, PioneeringProjectsInfo

# Register your models here.
@admin.register(OrganizationDetail)
class OrganizationDetailAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('tagline', 'email', 'phone', 'logo', 'location'),
            'classes': ('collapse',),
        }),
        ('Social Media Links', {
            'fields': ('facebook', 'instagram', 'twitter', 'linkedin'),
            'classes': ('collapse',),
        }),
        ('Mission & Vision', {
            'fields': ('mission', 'vision',),
            'classes': ('collapse',)
        })
    )

admin.site.register(WhatIsHCG)
admin.site.register(PioneeringProjectsInfo)

class GoalInline(admin.TabularInline):  # Use TabularInline or StackedInline
    model = Goal
    extra = 1  

@admin.register(ImportantGoals)
class ImportantGoalsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Short Description', {
            'fields': ('short_description',),
        }),
    )
    inlines = [GoalInline]