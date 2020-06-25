from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    username = None
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = []
class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)

class Ad(models.Model):
    def __str__(self):
        return self.title
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    text = models.CharField(max_length=1000, blank=False)
    price = models.PositiveIntegerField(blank=False)
    is_active = models.BooleanField(default=0)
    pub_date = models.DateTimeField(default=datetime.now, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Picture(models.Model):
    url = models.FileField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 

class Conversation(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="seller")
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="buyer")

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    sent_at = models.DateTimeField(default=datetime.now, blank=False)
    is_viewed = models.BooleanField(default=0)