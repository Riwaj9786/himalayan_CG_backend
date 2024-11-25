from django.contrib import admin
from api.models import Blog, Initiatives, OrganizationDetail

# Register your models here.
admin.site.register(OrganizationDetail)
admin.site.register(Blog)
admin.site.register(Initiatives)