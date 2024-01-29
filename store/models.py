from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class VideoItem(models.Model):

    video_title = models.CharField(max_length=255)
    video_description = models.TextField()
    # video_file = models.FileField(upload_to='upload_files/videos/', validators=[
    #     FileExtensionValidator(allowed_extensions=['mp4', 'ts', 'mov'])])
    video_url = models.URLField()
    video_thumbnail = models.ImageField(upload_to='upload_files/images/', validators=[
        FileExtensionValidator(allowed_extensions=['jpeg', 'png'])])
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_title
