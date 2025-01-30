
from django.db import models
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.TextField()
    message=models.TextField()

    def __str__(self):
        return self.email