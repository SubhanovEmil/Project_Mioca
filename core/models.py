from django.db import models

# Create your models here.

class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        abstract = True
        
class Contact(AbstractModel):

    first_name = models.CharField('First name', max_length = 100)
    last_name = models.CharField('Last name', max_length = 100)
    email = models.EmailField('E-mail', max_length = 100)
    message = models.TextField('Message', max_length = 100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"