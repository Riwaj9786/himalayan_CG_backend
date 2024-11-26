from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(
        max_length=155,
    )
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=555)
    message = RichTextUploadingField()
    is_accepted = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ('-submitted_at',)

    def __str__(self):
        return f"{self.full_name}: {self.subject}"