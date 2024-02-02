from django.contrib import admin
from administrator.models import Administrative_Data
# Register your models here.
from django.contrib.auth.models import User

admin.site.register(Administrative_Data)
#admin.site.register(User)