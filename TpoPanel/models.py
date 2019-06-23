from django.db import models
from django.contrib.auth.models import User


class TpoDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tpo_mobile = models.CharField(max_length=10)
