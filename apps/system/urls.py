from rest_framework.routers import  DefaultRouter
from . import  views


system_router = DefaultRouter()
system_router.register(r'tenants', views.TenantViewSet)
