from django.contrib import admin
from career.models import Career, CareerApply

# Register your models here.
@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'deadline', '_is_active')
    list_display_links = ('position_name', 'deadline', '_is_active')


admin.site.register(CareerApply)