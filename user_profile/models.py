from django.db import models

# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(max_length=200,null=True,blank=True,default="")
    last_name = models.CharField(max_length=200,null=True,blank=True,default="")
    avatar = models.CharField(max_length=200,null=True,blank=True,default="")
    phone_number = models.CharField(max_length=10,null=True,blank=True,default="")
    location = models.CharField(max_length=200,null=True,blank=True,default="")
    passport_pic = models.FileField(upload_to='user',null=True, blank=True)
    
    def __str__(self):
        return self.first_name + self.last_name
    