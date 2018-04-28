from rest_framework import authentication,permissions,viewsets,filters
from .models import Sprint,Task
from .serializers import SprintSerializer,TaskSerializer,UserSerializer
from django.contrib.auth import get_user_model
from .forms import TaskFilter, SprintFilter

User = get_user_model()

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




class SprintViewSet(DefaultsMixin,viewsets.ModelViewSet):
    """API endpoint for listing and creating sprints"""

    queryset = Sprint.objects.order_by('end')
    """序列化"""
    serializer_class =  SprintSerializer
    """查询过滤条件"""
    filter_class = SprintFilter
    search_fileds = ('name',)
    ordering_fileds = ('end','name',)




class TaskViewSet(DefaultsMixin,viewsets.ModelViewSet):
    """API endpoint for listing and creating tasks."""

    queryset = Task.objects.all()
    """序列化"""
    serializer_class = TaskSerializer
    """字段过滤条件"""
    filter_class = TaskFilter
    """查询搜索条件"""
    search_fileds = ('name','description',)
    """查询支持排序的字段"""
    ordering_fileds = ('name','order','started','due','completed',)



class UserViewSet(DefaultsMixin,viewsets.ReadOnlyModelViewSet):
    """API endpoint for listing users.."""
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg =  User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    search_fileds = (User.USERNAME_FIELD,)




