from django.db import models
from django.contrib.auth.models import User

class Music(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    author=models.CharField(max_length=150)
    musical_genre=models.CharField(max_length=70)

    def __str__(self):
        return self.name