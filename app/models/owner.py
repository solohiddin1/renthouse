from django.db import models
# from .user import User
from .house import BaseModel


class Owner(BaseModel):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    arena_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.name if self.user.name else self.user.email