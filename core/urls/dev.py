import debug_toolbar
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from .base import *

urlpatterns += [
    url(r'^__debug__/', include(debug_toolbar.urls)),
]

# serve static and media files on development
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
