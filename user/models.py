from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from core.models import AbstractModel


class User(AbstractUser):
    name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50, null=True, blank= True)
    email = models.EmailField("email address", unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    ips = ArrayField(models.GenericIPAddressField(), null=True, blank= True)
    
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = 'name',

    def get_profile_image(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return "/static/images/no_photo.jpg"

class BlockedIpAddress(AbstractModel):
    ip_address = models.GenericIPAddressField()
