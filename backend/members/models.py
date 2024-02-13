from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Member(models.Model):    
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=False,related_name='member_object')
    

