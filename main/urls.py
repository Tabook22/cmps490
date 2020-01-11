from django.urls import path

from .views import index,detail,pho_detail
app_name="main"
urlpatterns=[
    path('', index, name="main_page"),
    path('index/', index, name="main_page"),
    path('detail/', detail, name="detail"),
    path('detail/<int:id>', detail, name="detail"),
    path('pho_detail/<int:id>', pho_detail, name="pho_detail"),
    ]