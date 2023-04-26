from django.db import models

class Music(models.Model):
    name=models.CharField(max_length=150)
    author=models.CharField(max_length=150)
    musical_genre=models.CharField(max_length=70)

    def __str__(self):
        return self.name