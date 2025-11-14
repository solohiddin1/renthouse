from django.db import models
from .house import BaseModel

class Like(BaseModel):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    house = models.ForeignKey("House", on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'house')

    def __str__(self):
        return f"user {self.user.name} liked {self.house.name}"