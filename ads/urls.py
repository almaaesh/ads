from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views

from django.conf import settings
from django.conf.urls.static import static

import post.urls

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    # path('accounts/', include('accounts.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
