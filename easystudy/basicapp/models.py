from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=128,blank=False,default=' ')
    last_name=models.CharField(max_length=128,blank=False,default=' ')
    phone=models.CharField(max_length=10,blank=False,unique=True)
    street=models.CharField(max_length=256)
    city=models.CharField(max_length=128)
    code=models.CharField(max_length=128)
    state=models.CharField(max_length=128,default=' ')
    def __str__(self):
        return self.user.username
