

from django.contrib import admin
from django.conf import settings
from django.urls import include, path  # For django versions from 2.0 and up

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        # your urls
         path('admin/', admin.site.urls, name='admin'),
    path('', include('home.urls')),
    path('auth/', include("django.contrib.auth.urls")),
    path('accounts/', include('accounts.urls')),
    
    ]