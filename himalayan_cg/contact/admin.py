from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'submitted_at',)
    list_display_links = ('email', 'subject')
    search_fields = ('email', 'full_name')
    readonly_fields = ('full_name', 'email', 'phone_number', 'subject', 'message', 'submitted_at', 'is_accepted')