from django.db import models
from django.utils import timezone


class ContactMessage(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    submit_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def send(self):
        self.submit_date = timezone.now()
        self.save()
