from django.contrib import admin
from .models import VideoItem


# Register your models here.


class VideoItemAdmin(admin.ModelAdmin):

    list_display = ('video_title', 'video_description', 'upload_date')

admin.site.register(VideoItem, VideoItemAdmin)
