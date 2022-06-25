from django.shortcuts import render,redirect,HttpResponse
from app01.models import Admin
from app01.utils.bootstraps import Bootstrap
from io import BytesIO
from app01.utils.code import check_code

def admin_list(request):
    queryset=Admin.objects.all()
    return render(request,"admin_list.html",{"queryset":queryset})

class AdminModelForm(Bootstrap):
    class Meta:
        model=Admin
        fields="__all__"

def admin_add(request):
    '''管理员添加'''
    title="添加管理员"
    if request.method=="GET":
        form=AdminModelForm()
        return render(request,"change.html",{"form":form,"title":title})
    else:
        form=AdminModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/admin/list/")
        return render(request,"change.html",{"form":form})


def admin_delete(request,id):
    '''管理员删除'''
    Admin.objects.filter(id=id).delete()
    return redirect("/admin/list/")

def admin_edit(request,id):
    '''管理员编辑'''
    data=Admin.objects.filter(id=id).first()
    if request.method=="GET":
        form=AdminModelForm(instance=data)
        return render(request,"change.html",{"form":form})
    else:
        form=AdminModelForm(data=request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("/admin/list/")
        else:
            return render(request,"change.html",{"form":form})


class RestModelForm(Bootstrap):
    class Meta:
        model=Admin
        fields=["password"]
def admin_reset(request,id):
    '''重置密码'''
    title="重置密码"
    data=Admin.objects.filter(id=id).first()
    if request.method=="GET":
        form=RestModelForm()
        return render(request,"change.html",{"form":form,"title":title})
    form=RestModelForm(data=request.POST,instance=data)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")
    return render(request,"change.html",{"form":form})


def lagout(request):
    '''退出'''
    request.session.clear()
    return redirect("/login/")


from django import forms
class LoginForm(forms.Form):

    adminname=forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class":"form-control"}),
        required=True
    )
    password=forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={"class":"form-control"},render_value=True),
        required=True
    )

    code=forms.CharField(
        label="验证码",
        widget=forms.TextInput(attrs={"class":"form-control"}),
        required=True
    )

def login(request):
    '''登录'''
    if request.method=="GET":
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    form=LoginForm(data=request.POST)
    if form.is_valid():
        user_input_code=form.cleaned_data.pop("code")
        code = request.session.get("image_code","")
        if code.upper()!=user_input_code.upper():
            form.add_error("code","验证码错误")
            return render(request,"login.html",{"form":form})
        admin_object=Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password","用户或密码错误")
            return render(request,"login.html",{"form":form})
        else:
            request.session["info"]={"id":admin_object.id,"name":admin_object.adminname}
            #7天免登陆
            request.session.set_expiry(60*60*24*7)
            return redirect("/service/show/")
    return render(request,"login.html",{"form":form})

def image_code(request):
    '''生成随机验证码图片'''
    img,code_string=check_code()

    #将用户填写验证码写入到自己的session中(以便后续获取验证码再进行校验)
    request.session['image_code']=code_string
    # 给session设置60s超时
    request.session.set_expiry(60)

    # 将验证码文件写入内存中
    stream=BytesIO()
    img.save(stream,'png')
    # 将图片内容返回给浏览器
    return HttpResponse(stream.getvalue())




