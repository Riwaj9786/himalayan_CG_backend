from rest_framework import serializers
from career.models import Career, CareerApply, PositionType, JobLocation, JobType


class PositionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionType
        fields = ('id', 'position_type')
        read_only_fields = ('id',)

class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ('id', 'job_type')
        read_only_fields = ('id',)

class JobLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLocation
        fields = ('id', 'job_location')
        read_only_fields = ('id',)


class CareerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ('uuid', 'position_name', 'job_type', 'deadline')


class CareerDetailSerializer(serializers.ModelSerializer):
    job_location = JobLocationSerializer(read_only=True)
    job_type = JobTypeSerializer(read_only=True)
    position_type = PositionTypeSerializer(read_only=True)
    class Meta:
        model = Career
        fields = ('position_name', 'job_description', 'job_requirements', 'salary', '_is_active', 'position_type', 'job_type', 'job_location', 'opening_date', 'deadline')
        read_only_fields = ('opening_date', 'deadline')


class CareerApplySerializer(serializers.ModelSerializer):
    position = CareerDetailSerializer(read_only = True)
    
    class Meta:
        model = CareerApply
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'cv', 'position', 'submitted_at',)
        read_only_fields = ('submitted_at', 'position',)
