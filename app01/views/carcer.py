from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe

from app01.models import Depart


def carcer_list(request):
    '''职务列表'''

    data_dict={}
    search_data=request.GET.get('q',"")
    if search_data:
        data_dict["title__contains"]=search_data

    page = int(request.GET.get("page", "1"))  # 当前页
    page_size = 10  # 每页显示10条数据
    start = (page - 1) * 10
    end = page * 10
    total_count = Depart.objects.filter(**data_dict).order_by("-id").count()  # 数据总条数

    # 计算总页码
    total_page_count, div = divmod(total_count, page_size)
    if div > 1:  # 余数大于1
        total_page_count += 1

    # 分页第二步
    # 计算出,显示当前页的前5页,后5页
    plus = 5

    if total_page_count < 2 * plus + 1:
        # 当数据库的数据库比较少的时候,都没有达到11页
        start_page = 1
        end_page = total_page_count
    else:
        # 当前页小于5时
        if page <= plus:
            start_page = 1
            end_page = 2 * plus + 1
        # 当数据库的数据库比较多的时候
        else:
            # 当前页大于5时
            if page + plus > total_page_count:
                start_page = total_page_count - 2 * plus  # 往前推10个
                end_page = total_page_count
            else:
                start_page = page - plus
                end_page = page + plus + 1

    tpl_str_list = []

    # 首页
    prve = '<li><a href="?page={}">首页</a></li>'.format(1)
    tpl_str_list.append(prve)

    # 上一页
    if page > 1:
        prve = '<li><a href="?page={}">上一页</a></li>'.format(page - 1)
    else:
        prve = '<li><a href="?page={}">上一页</a></li>'.format(1)
    tpl_str_list.append(prve)

    for i in range(start_page, end_page + 1):
        if i == page:
            ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
        else:
            ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
        tpl_str_list.append(ele)

    # 下一页
    if page < total_page_count:
        prve = '<li><a href="?page={}">下一页</a></li>'.format(page + 1)
    else:
        prve = '<li><a href="?page={}">下一页</a></li>'.format(total_page_count)
    tpl_str_list.append(prve)

    # 尾页
    prve = '<li><a href="?page={}">尾页</a></li>'.format(total_page_count)
    tpl_str_list.append(prve)

    page_string = mark_safe("".join(tpl_str_list))

    queryset = Depart.objects.filter(**data_dict)[start:end]

    return render(request,"carcer_list.html",{"queryset":queryset,"search_data":search_data,"page_string":page_string})

from app01.utils.bootstraps import Bootstrap

class CarcerModelForm(Bootstrap):
    class Meta:
        model=Depart
        fields="__all__"

def carcer_add(request):
    '''添加职务'''
    title="添加职务"
    if request.method=="GET":
        form=CarcerModelForm()
        return render(request,"change.html",{"form":form,"title":title})
    form=CarcerModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/carcer/list/")
    return render(request,"change.htmll",{"form":form})

def carcer_delete(request,id):
    '''删除职务'''
    Depart.objects.filter(id=id).first()
    return render(request,"carcer_list.html")

def carcer_edit(request,id):
    '''编辑职务'''
    data=Depart.objects.filter(id=id).first()
    if request.method=="GET":
        form=CarcerModelForm(instance=data)
        return render(request,"change.html",{"form":form})
    form=CarcerModelForm(data=request.POST,instance=data)
    if form.is_valid():
        form.save()
        return redirect("/carcer/list/")
    return render(request,"change.html",{"form":form})
