from rest_framework import serializers
from UserProfile.models import Profile, Position, Team


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('uuid', 'name', 'image', 'phone', 'facebook', 'instagram', 'twitter', 'phone', 'email')
        read_only_fields = ('uuid', 'created_at', 'updated_at')


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('rank', 'position')


class MemberSerializer(serializers.ModelSerializer):
    position = PositionSerializer(read_only=True) 

    class Meta:
        model = Profile
        fields = ('name', 'image', 'position')


class TeamSerializer(serializers.ModelSerializer):
    profile = MemberSerializer(read_only=True, many=True)
    
    class Meta:
        model = Team
        fields = ('id', 'team_name', 'description', 'profile')
        read_only_fields = ('id', 'profile')