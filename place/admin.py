from django.contrib import admin

# Register your models here.
from .models import Place, Image, Comment, GustComment

admin.site.register(Place)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(GustComment)
