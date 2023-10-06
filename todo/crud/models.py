from django.db import models

# Create your models here.

class crud(models.Model):
    title = models.CharField(max_length=150)
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title