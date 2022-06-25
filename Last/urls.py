"""mysite3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from app01.views import admin,order,service,work,hotel,carcer,chart,info

from django.urls import path,re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [

    #配置上传文件路径
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT},name='media'),
    #服务展示
    path('service/list/', service.service_list),
    path('service/add/', service.service_add),
    path('service/<int:id>/edit/', service.service_edit),
    path('service/<int:id>/delete/', service.service_delete),
    path('service/show/',service.service_show),

    # 管理员管理
    path('admin/list/',admin.admin_list),
    path('admin/add/',admin.admin_add),
    path('admin/<int:id>/edit/',admin.admin_edit),
    path('admin/<int:id>/delete/',admin.admin_delete),
    path('admin/<int:id>/reset/',admin.admin_reset),

    #工作人员
    path('work/list/', work.work_list),
    path('work/add/', work.work_add),
    path('work/<int:id>/edit/',work.work_edit),
    path('work/<int:id>/delete/', work.work_delete),


    # 登录管理
    path('login/',admin.login),

    #注销
    path('lagout/',admin.lagout),

    # 订单管理
    path('order/list/',order.order_list),
    path('order/add/',order.order_add),
    path('order/delete/',order.order_delete),
    # path('order/detail/',order.order_detail),
    # path('order/edit/',order.order_edit),

    #酒席管理
    path('hotel/list/',hotel.hotel_list),
    path('hotel/add/',hotel.hotel_add),
    path('hotel/<int:id>/edit/', work.work_edit),
    path('hotel/<int:id>/delete/', work.work_delete),


    #职务管理
    path('carcer/list/',carcer.carcer_list),
    path('carcer/add/',carcer.carcer_add),
    path('carcer/<int:id>/delete/',carcer.carcer_delete),
    path('carcer/<int:id>/edit/',carcer.carcer_edit),

    #图片验证码
    path('image/code/',admin.image_code),


    #数据显示
    path('chart/list/',chart.chart_list),

    #个人信息
    path('info/people/',info.info_list),

    #注册
    path('register/',info.register),








]
