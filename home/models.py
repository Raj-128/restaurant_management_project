from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.Charfield(max_length=255)

    def_str(self):
        return self.name