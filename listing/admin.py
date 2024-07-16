from django.contrib import admin
from .models import Property, Picture, Location, ImportantFigures, ContactForm
# Register your models here.
admin.site.register(Property)
admin.site.register(Picture)
admin.site.register(Location)
admin.site.register(ImportantFigures)
admin.site.register(ContactForm)