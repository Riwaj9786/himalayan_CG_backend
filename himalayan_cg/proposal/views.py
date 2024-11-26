from django.shortcuts import render
from .models import Proposal
from .serializers import ProposalSerializer, ProposalApplySerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class ProposalListAPIView(ListAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    permission_classes = (IsAuthenticated,)


class ProposalCreateAPIView(CreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalApplySerializer
    permission_classes = (AllowAny,)