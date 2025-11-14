from django.contrib import admin
from app.models.house import House, HouseImages
from .models.owner import Owner
from .models.user import User
from .models.ratings import Rating
from .models.comment import Comment


# Register your models here.

# admin.site.register(Student)
admin.site.register(User)

class HouseImagesInline(admin.TabularInline):
    model = HouseImages
    extra = 3

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    inlines = [HouseImagesInline]

admin.site.register(Owner)
admin.site.register(Rating)
admin.site.register(Comment)