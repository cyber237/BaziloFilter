from django.contrib import admin
from .models import *

# Register your models here.
admin.sites.register([LeadEmailInfo,LeadPhoneInfo,Lead,APIUtils,InvalidName])
