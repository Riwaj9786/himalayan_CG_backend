from rest_framework import serializers
from .models import Contact

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'full_name', 'email', 'phone_number', 'subject', 'message', 'is_accepted', 'submitted_at')
        read_only_fields = ('id', 'submitted_at')

    def validate(self, data):
        if not data.get('is_accepted'):
            raise serializers.ValidationError('You must accept the Terms to Continue!')
        
        return data