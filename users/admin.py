from django.contrib import admin
from .models import Profile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'user_image',)

admin.site.register(Profile, UserProfileAdmin)