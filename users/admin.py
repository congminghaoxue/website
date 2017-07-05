from django.contrib import admin
from .models import UserModel
# Register your models here.
#
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'premium', 'fee', 'phone', 'phone_district')
    list_filter=('fee', 'premium', 'phone_district')
    search_fields = ('name', 'phone')

admin.site.register(UserModel, UserAdmin)
