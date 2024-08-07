from django.contrib import admin
from .models import UserComment, Booking, Menu

# Register your models here.
admin.site.register(UserComment)
admin.site.register(Booking)
admin.site.register(Menu)