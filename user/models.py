from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=50, null=True, blank= True)
    email = models.EmailField("email address", null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def get_profile_image(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return "/static/images/no_photo.jpg"