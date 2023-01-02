from django.contrib import admin
from .models import Agent,Location,Property,Propertycategory,Blog,Comment

admin.site.register(Agent),
admin.site.register(Location),
admin.site.register(Property),
admin.site.register(Propertycategory)
admin.site.register(Blog)
admin.site.register(Comment)

