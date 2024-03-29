"""
URL configuration for fatcorkbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers

from inventory.views.inventory import (
    CuveeViewSet,
    CuveeView,
    CuveeListView,
    VendorView,
    VendorListView,
)


router = routers.DefaultRouter()
router.register(r'cuvees', CuveeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('inventory/', include('inventory.urls')),
    path('', RedirectView.as_view(url='inventory/', permanent=True)),
    path('api-auth/', include('rest_framework.urls')),  # browsable API

    path('cuvee_list/', CuveeListView.as_view(), name='cuvee_list'),
    path('cuvee/<int:pk>', CuveeView.as_view(), name='cuvee'),
    path('vendor_list/', VendorListView.as_view(), name='vendor_list'),
    path('vendor/<int:pk>', VendorView.as_view(), name='vendor'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
