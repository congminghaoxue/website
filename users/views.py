from django.shortcuts import render
# from django.http import JsonResponse
# from django.core import serializers
# Create your views here.
# 导入模型中的UserModel表
from .models import UserModel

# Create your views here.

def users(request):
    # 获取所有的用户
    all_user = UserModel.objects.all()
    # 把用户信息和前端文件一起发送到浏览器

    """
    todo : response to json
    """
    # all_user = serializers.serialize('json', all_user, fields=('name','phone'))
    # return JsonResponse(dict(all_user))

    return render(request, 'users.html', {'all_user': all_user})
