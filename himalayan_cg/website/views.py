from .models import OrganizationDetail, WhatIsHCG, PioneeringProjectsInfo, ImportantGoals
from rest_framework.generics import ListAPIView
from .serializers import OrganizationDetailSerializer, ImportantGoalsSerializer, WhatIsHCGSerializer, PioneeringProjectsInfoSerializer

# Create your views here.
class OrganizationDetailListAPIView(ListAPIView):
    queryset = OrganizationDetail.objects.all()
    serializer_class = OrganizationDetailSerializer


class WhatIsHCGListAPIView(ListAPIView):
    queryset = WhatIsHCG.objects.first()
    serializer_class = WhatIsHCGSerializer


class PioneeringProjectsInfoListAPIView(ListAPIView):
    queryset = PioneeringProjectsInfo.objects.first()
    serializer_class = PioneeringProjectsInfoSerializer


class ImportantGoalsListAPIView(ListAPIView):
    queryset = ImportantGoals.objects.first()
    serializer_class = ImportantGoalsSerializer
