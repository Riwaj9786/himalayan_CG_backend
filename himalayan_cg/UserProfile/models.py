import os
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
    

class Profile(BaseModel):
    name = models.CharField(
        max_length=125,
        null=False,
        blank=False
    )
    image = models.ImageField(upload_to=file_to_upload_profile_picture, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='team_member')

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "user Profiles"

    def __str__(self):
        return f"{self.name}" 
    

    
class BoardOfDirectors(Profile):
    rank = models.IntegerField(unique=True, help_text="Lower the Rank, the higher the position is!")
    position = models.CharField(max_length=75)

    class Meta:
        ordering = ('rank',)
        verbose_name = "Board Member"
        verbose_name_plural = "Board of Directors"

    def __str__(self):
        return f"{self.position} | {self.name}"