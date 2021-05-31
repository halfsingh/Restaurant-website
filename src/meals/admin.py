from django.contrib import admin

# Register your models here.

from .models import Meals, category

admin.site.register(Meals)
admin.site.register(category)