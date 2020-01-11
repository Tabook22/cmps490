from django.urls import path, include
from .views import index, add_new_p, delete, editp, edit_p, search
app_name="pho"
urlpatterns = [
    path('', index),
    path('index/', index),
    path('add_new_p/', add_new_p),
    path('delete/<int:id>/',delete, name="delete"),
    path('editp/<int:id>/',editp, name="editp"),
    path('edit_p/', edit_p),
    path('search/', search),

]
