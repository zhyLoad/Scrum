from rest_framework import authentication,permissions,viewsets,filters
from .models import Tenant
from .serializers import TenantSerializer

"""通用基类，主要定义了授权、分页、排序、Filter定义等"""
class DefaultsMixin(object):
     """Default settings for view authetication,permissions,filtering and pagination."""

     authentication_classes =(
         authentication.BasicAuthentication,
         authentication.TokenAuthentication,
     )
     permission_classes = (
         permissions.IsAuthenticated,
     )
     paginate_by = 25
     paginate_by_param = 'page_size'
     max_paginate_by = 100
     filter_backends = (
         filters.DjangoFilterBackend,
         filters.SearchFilter,
         filters.OrderingFilter,
     )




class TenantViewSet(DefaultsMixin,viewsets.ModelViewSet):
    """API endpoint for listing and creating sprints"""

    queryset = Tenant.objects.order_by('create_time')
    """序列化"""
    serializer_class =  TenantSerializer
    search_fileds = ('name',)
    ordering_fileds = ('create_time','name',)
