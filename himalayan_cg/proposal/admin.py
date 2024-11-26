from django.contrib import admin
from .models import Proposal

# Register your models here.
@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('project', 'full_name', 'email', 'submitted_at')
    list_display_links = ('project', 'full_name', 'email')
    search_fields = ('project', 'full_name', 'email')
    list_filter = ('project_year',)
    readonly_fields = ('project', 'full_name', 'email', 'project_year', 'phone_number', 'proposal_document')

    fieldsets = (
        ("Your Information", {
            "fields": ("full_name", "email", "phone_number",),
        }),
        
        ("Proposal Details", {
            "fields": ("project", "proposal_document", "project_year",),
        }),
    )