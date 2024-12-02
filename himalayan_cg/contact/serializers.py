from rest_framework import serializers
from .models import Contact

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'full_name', 'email', 'phone_number', 'subject', 'message', 'submitted_at')
        read_only_fields = ('id', 'submitted_at')