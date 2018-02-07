from __future__ import unicode_literals
from django.utils.crypto import get_random_string

from django.contrib.auth.models import User

from django.db import models

# Create your models here.


class Room(models.Model):
    room_name = models.CharField(max_length=20)
    room_key = models.CharField(max_length=8, primary_key=True, default=get_random_string(length=8))
    users = models.ManyToManyField(User, related_name='%(class)s_users_in_room')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_room_creator', null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
