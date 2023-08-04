from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True )
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    isComplete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title