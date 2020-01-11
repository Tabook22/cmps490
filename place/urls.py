from django.urls import path, include
from .views import index, add_new_pl, delete, editpl, edit_pl, search,uploadimg,addcomment
app_name="place"
urlpatterns = [
    path('', index),
    path('index/', index),
    path('uploadimg/', uploadimg),
    path('add_new_pl/', add_new_pl),
    path('delete/<int:id>/',delete, name="delete"),
    path('editpl/<int:id>/',editpl, name="editpl"),
    path('edit_pl/', edit_pl),
    path('search/', search),
    path('addcomment/', addcomment, name="addcomment"),




]
