from rest_framework import serializers
from .models import Tenant
from rest_framework.reverse import reverse

class TenantSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()
    tenant_status_display = serializers.SerializerMethodField()
    delete_flag_display = serializers.SerializerMethodField()

    class Meta:
        model = Tenant
        fields = ('id','name','phone','account','description','tenant_status','tenant_status_display','delete_flag','delete_flag_display','links')

    def get_links(self,obj):
        request = self.context['request']
        return {
            'self': reverse('tenant-detail',kwargs={'pk':obj.pk},request=request),
        }
    def get_tenant_status_display(self,obj):
        return obj.get_tenant_status_display()
    def get_delete_flag_display(self,obj):
        return obj.get_delete_flag_display()