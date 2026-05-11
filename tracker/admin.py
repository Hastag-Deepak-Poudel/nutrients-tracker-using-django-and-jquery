from django.contrib import admin
from .models import Nutrients, FoodConsumed
# Register your models here.

admin.site.register(Nutrients)
admin.site.register(FoodConsumed)