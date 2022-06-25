from django.shortcuts import redirect,render,HttpResponse
from app01.models import Admin


def info_list(request):
    '''现实个人信息'''
    return render(request,"info_list.html")

def register(request):
    '''注册管理员'''
    if request.method=="GET":
        return render(request,"register.html")

    name=request.POST.get("name")
    password=request.POST.get("password")
    Admin.objects.create(adminname=name,password=password)
    return redirect("/login/")