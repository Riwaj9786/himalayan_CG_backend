from django.db import models
from django.utils import timezone
from datetime import timedelta
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class BaseCareerModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(default=(timezone.now()+timedelta(days=7))) 

    class Meta:
        abstract = True  
    
    # def save(self, *args, **kwargs):
    #     if not self.deadline:
    #         self.deadline = timezone.now()+timedelta(days=7)

    #     super().save(*args, **kwargs)


######### Career #########
# 1. Position name
# 2. created_at
# 3. deadline
# 4. description
# 5. salary
# 6. is_active

class Career(BaseCareerModel):
    position_type_choices = [
        ('Internship', 'Internship'),
        ('Entry Level', 'Entry Level'),
        ('Mid Level', 'Mid Level'),
        ('Senior Level', 'Senior Level'),
    ]
    job_type_choices = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    ]
    job_location_choices = [
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
        ('On-Site', 'On-Site'),
    ]
    position_name = models.CharField(max_length=255)
    description = RichTextUploadingField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    _is_active = models.BooleanField(default=True)
    position_type = models.CharField(max_length=40, choices=position_type_choices, null=True, blank=True)
    job_type = models.CharField(max_length=40, choices=job_type_choices, null=True, blank=True)
    job_location = models.CharField(max_length=40, choices=job_location_choices, null=True, blank=True)

    def __str__(self):
        return f"{self.position_name}"
    
    @property
    def is_active(self):
        return self._is_active and timezone.now() <= self.deadline

    def save(self, *args, **kwargs):
        if timezone.now() > self.deadline:
            self._is_active = False
        super().save(*args, **kwargs)


def upload_to_cv(instance, filename):
    # Generate path dynamically based on the `position_name` of the related `Career` instance
    position_name = instance.position.position_name if instance.position else 'unknown_position'
    return f'careers/cv/{position_name}/{filename}'


class CareerApply(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=115)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.BigIntegerField()
    position = models.ForeignKey(Career, on_delete=models.DO_NOTHING, related_name='apply_position')
    cv = models.FileField(upload_to=upload_to_cv)
    accepted = models.BooleanField(default= False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.position}"