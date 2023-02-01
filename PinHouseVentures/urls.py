from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Admin/', admin.site.urls),
    path('', include('base.urls')),
    path('AdminPanel/', include('adminSection.urls')),
    path('Auth/', include('authentication.urls'))

]

if settings.DEBUG:
     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)