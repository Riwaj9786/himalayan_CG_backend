from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class OrganizationDetail(models.Model):
    tagline = models.TextField(null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    logo = models.FileField(upload_to='organization/logo/', null=True, blank=True)
    location = models.TextField()
    facebook = models.URLField(null=True, blank=True)      
    instagram = models.URLField(null=True, blank=True)      
    twitter = models.URLField(null=True, blank=True)      
    linkedin = models.URLField(null=True, blank=True)

    mission = models.TextField()
    vision = models.TextField()

    class Meta:
        verbose_name_plural = '1. Organization Detail'

    def __str__(self):
        return "Himalayan Conservative Group"
    

class WhatIsHCG(models.Model):
    display_question = models.TextField()
    text = models.TextField()

    class Meta:
        verbose_name_plural = "2. Introduction"

    def __str__(self):
        return self.display_question
    

class PioneeringProjectsInfo(models.Model):
    short_description = models.TextField()
    founded = models.IntegerField()
    projects = models.IntegerField()
    communities = models.CharField(max_length=10)
    volunteers = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "3. Pioneering Projects Details"

    def __str__(self):
        return "Pioneering Projects Information"
    

class ImportantGoals(models.Model):
    short_description = models.TextField()

    class Meta:
        verbose_name = "Goal"
        verbose_name_plural = "4. Goals"

    def __str__(self):
        return "Goals"


class Goal(models.Model):
    important_goal = models.ForeignKey(ImportantGoals, related_name='goals', on_delete=models.RESTRICT)
    icon = models.FileField(upload_to='icons/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])
    title = models.CharField(max_length=255)
    abstract_description = models.TextField()

    def __str__(self):
        return self.title