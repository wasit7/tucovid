from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='profile')
    full_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=10)
    extra_attribute = JSONField(default=dict)

    def __str__(self):
        return self.full_name
