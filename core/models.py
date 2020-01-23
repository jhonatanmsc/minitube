from django.contrib.auth.models import User
from django.db import models
import datetime


class Theme(models.Model):
    descr = models.CharField(max_length=50)

    def __str__(self):
        return self.descr

    @property
    def score(self):
        thumbs_up = 0
        thumbs_down = 0
        for video in self.videos.all():
            thumbs_up += video.thumbs_up
            thumbs_down += video.thumbs_up
        return thumbs_up - (thumbs_down/2)


class Video(models.Model):
    title = models.CharField(max_length=50)
    media = models.FileField(upload_to='videos')
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)
    themes = models.ManyToManyField(Theme, related_name='videos', null=True, blank=True)
    descr = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='thumbnails', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='videos')

    def __str__(self):
        return f'{self.title}'

    def like(self):
        self.thumbs_up += 1
        return self.thumbs_up

    def dislike(self):
        self.thumbs_down += 1
        return self.thumbs_down

    @property
    def formated_created_at(self):
        return datetime.date.strftime(self.created_at, "%d / %m / %Y")
