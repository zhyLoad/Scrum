from django.db import models
from django.utils.translation import  ugettext_lazy as _
import django.utils.timezone as timezone


class BaseEntry(models.Model):
    """base class for other entry"""
    version = models.IntegerField(default=1)
    create_id = models.IntegerField(blank=True,default=0)
    create_time = models.DateTimeField(blank=False,default=timezone.now())
    modify_id = models.IntegerField(blank=True,default=0)
    modify_time = models.DateTimeField(blank=False,default=timezone.now())
    transaction_id = models.CharField(max_length=100,blank=True)
    server_name = models.CharField(max_length=100,blank=True)

    class Meta:
        abstract = True


class Tenant(BaseEntry,models.Model):
    """租户"""

    TENANT_STATUS_HAS_FROZEN = 0
    TENANT_STATUS_HAS_ACTIVATED = 1

    TENANT_STATUS_CHOICES = (
        (TENANT_STATUS_HAS_FROZEN,_('has been frozen')),
        (TENANT_STATUS_HAS_ACTIVATED,_('has been activated'))
    )

    DELETE_FLAG_INVALID = 0
    DELETE_FLAG_VALID = 1

    DELETE_FLAG_CHOICES = (
        (DELETE_FLAG_INVALID,_('invalid')),
        (DELETE_FLAG_VALID,_('valid'))
    )

    name =  models.CharField(max_length=100,blank=True,default='')
    phone = models.CharField(max_length=100,blank=True,default='')
    account = models.CharField(max_length=100,blank=False,default='')
    description =  models.CharField(max_length=2048,blank=True,default='')
    tenant_status = models.SmallIntegerField(choices=TENANT_STATUS_CHOICES,default=TENANT_STATUS_HAS_ACTIVATED)
    delete_flag = models.SmallIntegerField(choices=DELETE_FLAG_CHOICES,default=DELETE_FLAG_VALID)

    def __str__(self):
        return self.name