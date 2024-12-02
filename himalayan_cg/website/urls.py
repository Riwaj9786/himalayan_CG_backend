from django.urls import path
from .views import (
    OrganizationDetailListAPIView,
    WhatIsHCGListAPIView,
    PioneeringProjectsInfoListAPIView,
    ImportantGoalsListAPIView,
)

urlpatterns = [
    path('info/', OrganizationDetailListAPIView.as_view(), name='organization_info'),
    path('whatishcg/', WhatIsHCGListAPIView.as_view(), name='what_is_hCG'),
    path('projects_info/', PioneeringProjectsInfoListAPIView.as_view(), name='pioneer_projects_details'),
    path('goals/', ImportantGoalsListAPIView.as_view(), name='goals'),    
]