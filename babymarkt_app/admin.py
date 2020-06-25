from django.contrib import admin
from .models import Ad, Category, User, Picture
# Register your models here.

admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Picture)