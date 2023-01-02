from django.contrib import admin

# Register your models here.
from .models import Agent,Location,Property, Propertycategory

admin.site.register(Agent),
admin.site.register(Location),
admin.site.register(Property),
admin.site.register(Propertycategory)

