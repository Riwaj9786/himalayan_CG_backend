from rest_framework import serializers
from proposal.models import Proposal

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ('id', 'full_name', 'email', 'phone_number', 'project', 'proposal_document', 'submitted_at')
        read_only_fields = ('id', 'submitted_at', 'proposal_document')

class ProposalApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ('id', 'full_name', 'email', 'phone_number', 'project', 'proposal_document', 'submitted_at', 'is_accepted',)
        read_only_fields = ('id', 'submitted_at',)

    def validate(self, data):
        if not data.get('is_accepted'):
            raise serializers.ValidationError('You must accept the Terms to continue!')
        
        return data