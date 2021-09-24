from django.db import models

# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y')
    created_at = models.DateTimeField(auto_now_add=True)
    button_navigate = models.CharField(max_length=200, default='https://www.google.com')

    def __str__(self):
        return self.headline
