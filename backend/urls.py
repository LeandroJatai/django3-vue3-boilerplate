from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path, include
from django.views.generic.base import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import backend.core.urls


urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),

    path('', include(backend.core.urls)),

    re_path(r'^.*$', TemplateView.as_view(template_name='base.html')),
]
