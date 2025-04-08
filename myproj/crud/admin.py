from django.contrib import admin
from .models import Recruiter,Job,JobDelegation

# Register your models here.
admin.site.register(Recruiter)
admin.site.register(Job)
admin.site.register(JobDelegation)