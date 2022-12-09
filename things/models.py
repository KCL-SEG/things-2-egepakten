from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=36, unique=True, blank=False)
    description = models.CharField(max_length=121, blank=False)
    quantity = models.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(50)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
