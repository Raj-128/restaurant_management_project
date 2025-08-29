from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='restaurant_logos/',blank=True,null=True)
    opening_hours = models.JSONField(default=dict,blank=True, null=True)
    
    def __str__(self):
        return self.name

class Restaurantlocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str__(self):
        returnf"{self.address},{self.city},{self.state} - {self.zip_code}"

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField() 
    message = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name = "Contact Submission "
        verbose_name_plural = "Contact Submissions"

        def __str__(self):
            return f"{self.name} - {self.email}"


class Feedback(models.Model):
    name = models.CharField(max_length=200)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = " Feedback"
        verbose_name_plural = " Feedbacks"

    def __str__(self):
        return f"feedback from {self.name} on {self.created_At.strftime('%Y-%m-%d')}"


