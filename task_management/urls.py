"""task_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib import admin
from django.urls import path, include

import task_management.api_v1 as api_v1


class HealthCheckAPIView(APIView):
    """Health Check for the API"""

    def get(self, request):
        return Response(data={"status": "Hello world!"}, status=status.HTTP_200_OK)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HealthCheckAPIView.as_view(), name='health-check'),
    path('', include((api_v1, 'task_management'), namespace='api_v1')),
    # API Schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
