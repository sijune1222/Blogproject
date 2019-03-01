from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'images/')
    image_thumbnail = ImageSpecField(source = 'image', processors=[ResizeToFill(120, 100)])
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.title