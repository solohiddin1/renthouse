from django.db import models
# from .owner import Owner
# from .ratings import Rating


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class House(BaseModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, related_name='houses')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.ForeignKey('Rating', on_delete=models.CASCADE, default=0.0, blank=True, null=True,  related_name="house_ratings")
    # comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='houses', blank=True, null=True)

    def __str__(self):
        return self.name if self.name else 'house'

class HouseImages(BaseModel):
    images = models.ImageField(upload_to='house_photos/', height_field=None, width_field=None, max_length=None, default='photos/default.jpg')
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_images')
