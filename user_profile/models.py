from django.db import models

# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(max_length=200,null=True,blank=True,default="")
    last_name = models.CharField(max_length=200,null=True,blank=True,default="")
    avatar = models.CharField(max_length=200,null=True,blank=True,default="")
    phone_number = models.CharField(max_length=10,null=True,blank=True,default="")
    location = models.CharField(max_length=200,null=True,blank=True,default="")
    file = models.FileField(null=True, blank=True)
    # s3_object_key_id = models.CharField(max_length=200,null=True,blank=True,default="")
    
    def __str__(self):
        return self.first_name + self.last_name
    