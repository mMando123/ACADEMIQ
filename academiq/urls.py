"""
Main URL configuration for academiq project.
Bilingual support: English (EN) & Arabic (AR)
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

# Non-translated URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/setlang/', set_language, name='set_language'),
]

# Translated URLs (with language prefix)
urlpatterns += i18n_patterns(
    path('', include('core.urls')),
    prefix_default_language=False,  # Don't prefix default language (en)
)

# Custom error handlers
handler404 = 'core.views.custom_404'
handler500 = 'core.views.custom_500'

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
