from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Optional image
    video = models.FileField(upload_to='videos/', blank=True, null=True)  # Optional video
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
