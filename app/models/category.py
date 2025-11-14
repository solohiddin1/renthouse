from django.db import models
from .house import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name