from rest_framework import serializers
from UserProfile.models import Profile, BoardOfDirectors, Team

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('id', 'name', 'image', 'phone', 'facebook', 'instagram', 'twitter', 'phone', 'email')
        read_only_fields = ('id',)


class BoardOfDirectorSerializer(serializers.ModelSerializer):
    rank = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = BoardOfDirectors
        fields = ('id', 'name', 'image', 'position', 'rank', 'phone', 'facebook', 'instagram', 'twitter', 'phone', 'email')
        read_only_fields = ('id',)


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'team_name', 'description')
        read_only_fields = ('id',)