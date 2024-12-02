from django.db import models
import uuid

# Create your models here.
class FrequentlyAskedQuestions(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "Frequently Asked Questions"

    def __str__(self):
        return f"{self.question}?: {self.answer}"
    