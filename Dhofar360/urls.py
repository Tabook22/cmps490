from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('index/', include('main.urls')),
    path('main/', include('main.urls')),
    path('admin/', admin.site.urls),
    path('pho/', include('pho.urls')),
    path('place/', include('place.urls')),

]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
