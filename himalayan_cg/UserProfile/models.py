import os
import uuid
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Team(models.Model):
    team_name = models.CharField(
        max_length=30,
        unique=True,
    )
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.team_name


def file_to_upload_profile_picture(instance, filename):
    name = instance.name

    return os.path.join('profile_pics/', f"{name}_{filename}")
    

    
class Position(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    rank = models.IntegerField(unique=True, help_text="Lower the Rank, the higher the position is!")
    position = models.CharField(max_length=75)

    class Meta:
        ordering = ('rank',)
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __str__(self):
        return f"{self.position}"
    


class Profile(BaseModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(
        max_length=125,
        null=False,
        blank=False
    )
    image = models.ImageField(upload_to=file_to_upload_profile_picture, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    email = models.EmailField()
    position = models.ForeignKey(Position, on_delete=models.PROTECT, null=True, blank=True, related_name='profile_position')
    team = models.ForeignKey(Team, on_delete=models.PROTECT, null=True, blank=True, related_name='team_member')

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return f"{self.name}"