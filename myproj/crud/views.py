from django.shortcuts import render
from rest_framework import viewsets
from .models import Recruiter, Job, JobDelegation
from .serializer import RecruiterSerializer, Jobserializer, JobDelegationserializer

class RecruiterViewSet(viewsets.ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = Jobserializer

class JobDelegationViewSet(viewsets.ModelViewSet):
    queryset = JobDelegation.objects.all()
    serializer_class = JobDelegationserializer
