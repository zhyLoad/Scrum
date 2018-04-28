from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Sprint,Task
from django.contrib.auth import get_user_model

User = get_user_model()




class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name',read_only=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id',User.USERNAME_FIELD,'full_name','is_active','links')

    """定义链接函数"""
    def get_links(self,obj):
        request = self.context['request']
        username = obj.get_username()
        return {
            'self': reverse('user-detail',kwargs={User.USERNAME_FIELD:username},request=request),
            'tasks': '{}?assigned={}'.format(reverse('task-list', request=request),username),
        }


class SprintSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Sprint
        fields = ('id','name','description','end','links')

    """定义链接函数"""
    def get_links(self,obj):
        request = self.context['request']
        return {
            'self': reverse('sprint-detail',kwargs={'pk':obj.pk},request=request),
            'tasks':reverse('task-list',request=request) + '?sprint={}'.format(obj.pk),
        }


class TaskSerializer(serializers.ModelSerializer):

    assigned = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD,required=False,allow_null= True,queryset=User.objects.all()
    )
    status_display = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id','name','description','sprint','status','status_display','order','assigned','started','due','completed','links')

    """定义显示枚举"""
    def get_status_display(self,obj):
        return obj.get_status_display()

    """定义链接函数"""
    def get_links(self,obj):
        request = self.context['request']
        links = {
            'self': reverse('task-detail',kwargs={'pk':obj.pk},request=request),
            'sprint': None,
            'assigned':None
        }
        if obj.sprint_id:
            links['sprint'] = reverse('sprint-detail',kwargs={'pk':obj.sprint_id},request=request),
        if obj.assigned_id:
            links['assigned'] = reverse('user-detail',kwargs={User.USERNAME_FIELD:obj.assigned_id},request=request),
        return {
            'self': reverse('task-detail',kwargs={'pk':obj.pk},request=request),
        }