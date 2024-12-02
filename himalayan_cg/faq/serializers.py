from rest_framework import serializers
from faq.models import FrequentlyAskedQuestions

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyAskedQuestions
        fields = ('uuid', 'question', 'answer')
        read_only_fields = ('uuid',)