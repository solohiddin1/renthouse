from django.db import models
from .house import BaseModel

class Rating(BaseModel):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    house = models.ForeignKey("House", on_delete=models.CASCADE, related_name='ratings',null=True)
    rating = models.PositiveSmallIntegerField(default=0, choices=[(i, i) for i in range(1, 6)], blank=True, null=True)  # 1-5
    # comment = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'house')

    def __str__(self):
        return f"user {self.user.name} rated {self.house.name} with {self.rating}"