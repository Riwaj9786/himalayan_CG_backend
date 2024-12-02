from rest_framework import serializers
from .models import OrganizationDetail, WhatIsHCG, PioneeringProjectsInfo, Goal, ImportantGoals

class OrganizationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDetail
        fields = ('tagline', 'email', 'phone', 'logo', 'location', 'facebook', 'instagram', 'twitter', 'linkedin', 'mission', 'vision')


class WhatIsHCGSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatIsHCG
        fields = ('display_question', 'text',)


class PioneeringProjectsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PioneeringProjectsInfo
        fields = ('short_description', 'founded', 'projects', 'communities', 'volunteers',)


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('important_goal', 'icon', 'title', 'abstract_description')


class ImportantGoalsSerializer(serializers.ModelSerializer):
    
    goals = GoalSerializer(many=True, read_only=True)
    
    class Meta:
        model = ImportantGoals
        fields = ('short_description', 'goals')