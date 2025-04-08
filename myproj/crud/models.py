from django.db import models

# Create your models here.
class Recruiter(models.Model):  # Capitalize model names
   name = models.CharField(max_length=200)
   email = models.EmailField(unique=True)
   password = models.CharField(max_length=200)
   mobile = models.IntegerField(null=True, blank=True)
   userpic = models.TextField(null=True, blank=True)
   is_deleted = models.BooleanField(default=False)
   user_created = models.DateField(auto_now_add=True)  # Automatically set creation date

   def __str__(self):
      return self.name

class Job(models.Model):
   jobtitle =  models.CharField(max_length=100,null=True, blank=True)
   experience = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
   expect_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) #client rate
   location = models.CharField(max_length=200, null=True, blank=True)
   jobdesc = models.TextField(null=True,blank=True)
   jobclient = models.CharField(max_length=100, null=True,blank=True)


class JobDelegation(models.Model):
    jobid = models.ForeignKey('Job', on_delete=models.CASCADE, related_name='language', null=True, blank=True)
    jobassign = models.ManyToManyField('Recruiter', related_name="assigned_recruiters", blank=True)
    jobdelegationdate = models.DateField(auto_now_add=True)
