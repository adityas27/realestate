from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('agent', 'Agent'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    wishlist = models.JSONField(default=list, null=True, blank=True)
    def __str__(self):
        return self.user.username
