from django.db import models
from django.utils import timezone
from datetime import timedelta
from ckeditor_uploader.fields import RichTextUploadingField
import uuid

class BaseCareerModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    opening_date = models.DateTimeField(default=timezone.now())
    deadline = models.DateTimeField(default=(timezone.now()+timedelta(days=7))) 

    class Meta:
        abstract = True  

######### Career #########
# 1. Position name
# 2. created_at
# 3. deadline
# 4. description
# 5. salary
# 6. is_active

class PositionType(models.Model):
    position_type = models.CharField(max_length=75, help_text='E.g. Internship, Entry Level, Mid Level, Senior Level')

    def __str__(self):
        return self.position_type
    

class JobType(models.Model):
    job_type = models.CharField(max_length=125, help_text='(E.g. Full Time, Part Time)')

    def __str__(self):
        return self.job_type


class JobLocation(models.Model):
    job_location = models.CharField(max_length=125, help_text='(E.g. On-Site, Remote, Hybrid)')

    def __str__(self):
        return self.job_location


class Career(BaseCareerModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    position_name = models.CharField(max_length=255)
    job_description = RichTextUploadingField()
    job_requirements = RichTextUploadingField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    _is_active = models.BooleanField(default=True)
    position_type = models.ForeignKey(PositionType, on_delete=models.PROTECT, name='position_type')
    job_type = models.ForeignKey(JobType, on_delete=models.PROTECT, name='job_type')
    job_location = models.ForeignKey(JobLocation, on_delete=models.PROTECT, name='job_location')

    def __str__(self):
        return f"{self.position_name}"
    
    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "1. Vacancies"

    @property
    def is_active(self):
        return self._is_active and timezone.now() <= self.deadline

    def save(self, *args, **kwargs):
        if timezone.now() > self.deadline:
            self._is_active = False
        super().save(*args, **kwargs)


def upload_to_cv(instance, filename):
    position_name = instance.position.position_name if instance.position else 'unknown_position'
    return f'careers/cv/{position_name}/{filename}'


class CareerApply(models.Model):
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Prefer Not To Say', 'Prefer Not To Say'),
    ]

    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=115)
    email = models.EmailField(null=False, blank=False)
    gender = models.CharField(max_length=55, choices=gender_choices)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.BigIntegerField()
    position = models.ForeignKey(Career, on_delete=models.PROTECT, related_name='apply_position')
    cv = models.FileField(upload_to=upload_to_cv)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.position}"

    
    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "2. Applications"