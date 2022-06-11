from django.db import models
from django.contrib.auth import get_user_model
from numpy import blackman
from datetime import datetime
import uuid


# Creating the database table

# In django anytime you make changes to your models
# make migrations
# -python manage.py makemigrations

## AFTER YOU HAVE MADE YOUR MIGRATIONS
# -python manage.py migrate

## CREATE AN ADMIN PANEL
# -python manage.py createsuperuser

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    # use connects to foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    

    # method to return the object's stored name
    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    num_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user