from django.contrib import admin
from api.models import Blog, Initiatives, OrganizationDetail, FAQ

# Register your models here.
admin.site.register(OrganizationDetail)
admin.site.register(Blog)
admin.site.register(Initiatives)
admin.site.register(FAQ)