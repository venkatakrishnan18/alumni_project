from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import *
from django.contrib.auth.models import User 
from django.contrib.auth.models import Group

# admin.site.unregister(Group)  # Unregister the Group model
# admin.site.unregister(User)  # Unregister the User model


admin.site.register(Registration)
admin.site.register(Event)
admin.site.register(Meeting)
admin.site.register(JobNotification)
admin.site.register(ContactMessage)
admin.site.register(Feedback)
