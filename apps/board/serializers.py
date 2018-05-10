from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Sprint,Task
from datetime import date
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

    """校验参数end :创建Sprint的时候end不能比当前日期小
       校验参数函数的定义固定格式：validate_<field> 
    """
    def validate_end(self,value):
        new =  self.instance is None
        changed = self.instance and self.instance.end != value
        if(new or changed) and (value< date.today()):
            msg = ('End date cannot be in the past.')
            raise serializers.ValidationError(msg)
        return value


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

    """确保Sprint在任务完成前不被修改，而且任务也不会分配给已完成的sprint"""
    def validate_sprint(self,value):
        if self.instance and self.instance.pk:
            if value!= self.instance.sprint:
                if self.instance.status == Task.STATUS_DONE:
                    msg = ('Cannot change the sprint of a completed task')
                    raise serializers.ValidationError(msg)
                if value and value.end < date.today():
                    msg = ('Cannot assign task to past sprints.')
                    raise serializers.ValidationError(msg)
        else:
            if value and value.end < date.today():
                msg = ('Cannot add tasks to past sprints.')
                raise serializers.ValidationError(msg)
        return value

    """涉及多个字段的校验使用validate函数定义"""
    """确保字段的组会对任务有意义"""
    def validate(self,attrs):
        sprint = attrs.get('sprint')
        status = attrs.get('status',Task.STATUS_TODO)
        started = attrs.get('started')
        completed = attrs.get('completed')
        if not sprint and status != Task.STATUS_TODO:
            msg = ('Backlog task must have "Not Started" status.')
            raise serializers.ValidationError(msg)
        if started and status!= Task.STATUS_TODO:
            msg = ('Started date cannot be set for not started tasks.')
            raise serializers.ValidationError(msg)
        if completed and status!= Task.STATUS_DONE:
            msg = ('Completed date cannot be set for uncompleted tasks.')
            raise serializers.ValidationError(msg)
        return attrs



