from rest_framework import serializers
from career.models import Career, CareerApply

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ('id', 'position_name', 'description', 'salary', '_is_active', 'position_type', 'job_type', 'job_location', 'deadline')
        read_only_fields = ('created_at',)


class CareerApplySerializer(serializers.ModelSerializer):
    position = CareerSerializer(read_only = True)
    
    class Meta:
        model = CareerApply
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'cv', 'accepted', 'position', 'submitted_at',)
        read_only_fields = ('submitted_at', 'position',)

    def validate(self, data):
        if not data.get('accepted'):
            raise serializers.ValidationError('You must accept the Terms to continue!')
        
        return data