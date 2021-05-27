from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('auth', obtain_auth_token),
    path('hub/', include('apps.hub.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls'))
]
