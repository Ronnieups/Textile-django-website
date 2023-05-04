from site import USER_BASE
from django.db import models
from django.contrib.auth.models import  BaseUserManager
from django.contrib.auth.models import AbstractUser


#class CustomUserManager(BaseUserManager):
    #def create_user(self, mobile_no, password=None, **extra_fields):
     #f not mobile_no:
        #raise ValueError('The mobile_no field must be set')
     #mobile_no = self.normalize_mobile_no(mobile_no)
     #user = self.model(mobile_no=mobile_no, **extra_fields)
     #user.set_mobile_no(mobile_no)
     #user.save(using=self._db)
     #return user
    
    #def create_superuser(self, mobile_no, password=None, **extra_fields):
       #extra_fields.setdefault('is_staff',True)
       #extra_fields.setdefault('is_superuser',True)
       #return self.create_user(self, mobile_no, password=None, **extra_fields)

class Profile(AbstractUser):
   user = models.OneToOneField(USER_BASE, on_delete=models.CASCADE)
   mobile_no =models.TextField(max_length=10,unique=True)   
   first_name = models.CharField(max_length=30)
   last_name = models.CharField(max_length=30)
   location = models.CharField(max_length=50,null =True, blank=True)
   alternative_mobile_no =models.TextField(max_length=10,unique=True,null=True, blank=True)
   broker_mobile_num = models.TextField(max_length=10,unique=True,null=True, blank=True)
   

   USERNAME_FIELD = 'mobile_no'
   REQUIRED_FIELDS = ['first_name','last_name']

   def __str__(self):
      return self.mobile_no
   
   def get_full_name(self):
      return f'{self.first_name} {self.last_name}'
