from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=200)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = " Feedback"
        verbose_name_plural = " Feedbacks"

    def __str__(self):
        return f"feedback from {self.name} on {self.created_At.strftime('%Y-%m-%d')}"


