from django.contrib.auth.models import User
from django.db import models

class Administrative_Data(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,)
    dob = models.DateField()
    sex = models.CharField(max_length=1,default="O")
    mobile_number = models.CharField(max_length=15, null=True, blank=True)


    
