from django.db import models


class Like(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    house = models.ForeignKey("House", on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'house')

    def __str__(self):
        return f"user {self.user.name} liked {self.house.name}"