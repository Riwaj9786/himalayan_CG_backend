from django.contrib import admin
from career.models import Career, CareerApply, PositionType, JobLocation, JobType

# Register your models here.
@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'deadline', '_is_active')
    list_display_links = ('position_name', 'deadline', '_is_active')
    search_fields = ('position_name',)
    list_filter = ('_is_active',)
    exclude = ('uuid',)


@admin.register(CareerApply)
class CareerApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender', 'get_position',)
    list_display_links = ('first_name', 'last_name', 'email', 'gender', 'get_position')
    list_filter = ('position__position_name', 'gender')
    search_fields = ('first_name', 'last_name', 'email', 'position__position_name')
    readonly_fields = ('position', 'first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'phone_number', 'cv')
    
    def get_position(self, obj):
        return obj.position.position_name
    get_position.short_description = 'Position'


# admin.site.register(PositionType)
# admin.site.register(JobType)
# admin.site.register(JobLocation)
