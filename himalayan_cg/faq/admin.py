from django.contrib import admin
from faq.models import FrequentlyAskedQuestions

# Register your models here.
@admin.register(FrequentlyAskedQuestions)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    list_display_links = ('question', 'answer')
    search_fields = ('question',)