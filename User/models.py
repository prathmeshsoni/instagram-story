from django.db import models


class StoryModel(models.Model):
    username = models.TextField()
    story_time = models.TextField()
    story_id = models.BigIntegerField(unique=True)
    story_link = models.TextField(null=True)
    tag_list = models.TextField(null=True)
    testing_time = models.DateField(blank=True, null=True)
    media_path = models.TextField(blank=True)
