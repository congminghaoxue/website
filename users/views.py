from django.shortcuts import render, HttpResponse
# from django.http import JsonResponse
from django.core import serializers
# Create your views here.
# 导入模型中的UserModel表
from .models import UserModel

# Create your views here.

def users(request):
    # 获取所有的用户
    all_user = UserModel.objects.all() #values('name')

    """
    todo : response to json
    """
    # XMLSerializer = serializers.get_serializer("xml")
    # xml_serializer = XMLSerializer()
    # xml_serializer.serialize(all_user)
    # data = xml_serializer.getvalue()

    data = serializers.serialize('json', all_user, fields=('name'))

    # 把用户信息和前端文件一起发送到浏览器
    return HttpResponse(data)

    return render(request, 'users.html', {'all_user': all_user})
