from  django.shortcuts import render
from django.http import JsonResponse

def chart_list(request):
    '''数据显示'''
    return render(request,"chart_list.html")
