from django.contrib import admin

# Register your models here.

from .models import Photographer, Uploadimg

admin.site.register(Photographer)
admin.site.register(Uploadimg)
