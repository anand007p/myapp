from django.db import models

class User(models.Model):  # Capitalize model names
   name = models.CharField(max_length=200)
   email = models.EmailField(unique=True)
   password = models.CharField(max_length=200)
   mobile = models.IntegerField(null=True, blank=True)
   userpic = models.TextField(null=True, blank=True)
   user_created = models.DateField(auto_now_add=True)  # Automatically set creation date

   def __str__(self):
      return self.name
