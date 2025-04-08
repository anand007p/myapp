from rest_framework import viewsets
from rest_framework import serializers
from .models import Job, JobDelegation,Recruiter


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = '__all__'


class Jobserializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobDelegationserializer(serializers.ModelSerializer):
    class Meta:
        model = JobDelegation
        fields = '__all__'

    jobid = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())  # Reference Job by ID
    jobassign = serializers.PrimaryKeyRelatedField(many=True, queryset=Recruiter.objects.all())  # Reference multiple Recruiters by ID

    # Custom create method to handle ManyToManyField for jobassign.
    def create(self, validated_data):
        # print(validated_data,"--------validated_data")
        recruiters = validated_data.pop('jobassign', [])
        job_delegation = JobDelegation.objects.create(**validated_data)
        job_delegation.jobassign.set(recruiters)  # Assign recruiters after creation
        return job_delegation

    # Custom update method to handle ManyToManyField for jobassign.
    def update(self, instance, validated_data):
        recruiters = validated_data.pop('jobassign', None)
        instance = super().update(instance, validated_data)
        if recruiters is not None:
            instance.jobassign.set(recruiters)  # Update recruiters
        return instance
    
