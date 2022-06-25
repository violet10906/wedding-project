from django.shortcuts import render
from app01.models import Order
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app01.utils.bootstraps import Bootstrap
import random
from datetime import datetime



class OrderForm(Bootstrap):
    class Meta:
        model=Order
        exclude=["oid"]

def order_list(request):
    '''订单表'''
    queryset=Order.objects.filter().all()
    form=OrderForm()
    context={"form":form,"queryset":queryset}
    return render(request,"order.html",context)

@csrf_exempt
def order_add(request):
    '''订单添加'''
    form=OrderForm(data=request.POST)
    if form.is_valid():
        # 额外增加一些非用户输入的值
        form.instance.oid=datetime.now().strftime("%Y%m%d%H%M%S")+str(random.randint(1000,9999))
        form.save()
        return JsonResponse({"status":True})
    #为我们序列化一个json的格式
    return JsonResponse({"status":False,'error':form.errors})

def order_delete(request):
    '''删除订单'''
    nid=request.GET.get("nid")
    exists=Order.objects.filter(id=nid).exists()
    if not exists:
        return JsonResponse({"status":False,'error':"数据不存在"})
    Order.objects.filter(id=nid).delete()
    return JsonResponse({"status":True})

# def order_detail(request):
#     '''编辑订单'''
#     nid=request.GET.get("nid")
#     row_dict=Order.objects.filter(id=nid).values("name","datatime","phone","address","status_choice","level_choice").first()
#     if not row_dict:
#         return JsonResponse({"status":False,'error':"数据不存在"})
#     result={
#         "status":True,
#         "data":row_dict
#     }
#     return JsonResponse(result)

# @csrf_exempt
# def order_edit(request):
#     '''编辑订单'''
#     nid=request.GET.get("nid")
#     row_object=Order.objects.filter(id=nid).first()
#     if not row_object:
#         return JsonResponse({"status":False,'tips':"数据不存在"})
#     form=OrderForm(data=request.POST,instance=row_object)
#     if form.is_valid():
#         form.save()
#         return JsonResponse({"status":True})
#     return JsonResponse({"status":False,'error':form.errors})



