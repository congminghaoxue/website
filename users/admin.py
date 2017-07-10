# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import UserModel
# Register your models here.
#

from .models import ProfileModel

class ProfileInline(admin.StackedInline):
    model = ProfileModel
    can_delete = False
    verbose_name_plural = 'profilemodel'
    fk_name = 'user'




class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileInline, )
    list_select_related = ('profilemodel', )

    def get_location(self, instance):
        return instance.profilemodel.district
    get_location.short_description = '地区'
    def get_chg_times(self, instance):
        return instance.profilemodel.chg_times
    get_chg_times.short_description = '可修改次数'
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)
    list_display = ('name', 'premium', 'fee', 'phone', 'phone_district', 'get_location','get_chg_times')
    list_filter=('fee', 'premium', 'profilemodel__district', 'profilemodel__chg_times')
    search_fields = ('name', 'phone')

admin.site.register(UserModel, UserAdmin)
