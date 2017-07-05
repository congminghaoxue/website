from django.shortcuts import render

# Create your views here.
# 导入模型中的UserModel表
from .models import UserModel

# Create your views here.

def users(request):
    # 获取所有的用户
    all_user = UserModel.objects.all()
    # 把用户信息和前端文件一起发送到浏览器
    return render(request, 'users.html', {'all_user': all_user})
