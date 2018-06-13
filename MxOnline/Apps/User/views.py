from django.shortcuts import render
from django.contrib.auth import authenticate,login

# Create your views here.

def login(request):
    # 点击链接时返回页面
    if request.method == "GET":
        return render(request, "login.html", {})
    # 发送表单时获取数据
    elif request.method == "POST":
        user_name = request.POST.get("username","")
        pass_word = request.POST.get("password","")

        # 使用Django的用户认证方法.
        user = authenticate(username=user_name, password=pass_word)
        if user:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "index.html")