from django.db import models

# Create your models here.
class ServiceCar(models.Model):
    '''婚车表'''
    num=models.IntegerField(verbose_name="数量")
    typeCar=models.CharField(verbose_name="品牌",max_length=32)
    price=models.DecimalField(max_digits=10, decimal_places=2,verbose_name="价格")
    status=(
        (0,"已占用"),
        (1,"待占用")
    )
    status_choice=models.SmallIntegerField(verbose_name="状态",choices=status,default=1)
    colour=models.CharField(verbose_name="颜色",max_length=32)

class Hotel(models.Model):
    '''酒席表'''
    num=models.IntegerField(verbose_name="数量")
    wine=models.CharField(verbose_name="酒种",max_length=64)
    price=models.DecimalField(max_digits=10, decimal_places=2,verbose_name="价格")
    wine_choice=(
        (0,"500"),
        (1,"800"),
        (2,"1000"),
        (3,"1200")
    )
    wine_type=models.SmallIntegerField(verbose_name="类型",choices=wine_choice,default=1)

class Depart(models.Model):
    '''部门表'''

    title = models.CharField(max_length=32, verbose_name="职务名称")

    def __str__(self):
        return self.title

class Work(models.Model):
    '''工作人员录入表'''
    name=models.CharField(max_length=64,verbose_name="姓名")
    choice=(
        (0,"男"),
        (1,"女")
    )
    gender=models.SmallIntegerField(default=0,verbose_name="性别",choices=choice)
    cancer=models.ForeignKey(verbose_name="职务",to=Depart,to_field="id",on_delete=models.CASCADE)
    phone=models.CharField(max_length=64,verbose_name="电话")
    address=models.CharField(verbose_name="地址",max_length=64)
    password=models.CharField(verbose_name="密码",max_length=64)
    #本质上还是CharField，自动保存数据
    photo=models.FileField(verbose_name="照片",max_length=128,upload_to="photo/")

class Admin(models.Model):
    '''管理员管理'''
    adminname=models.CharField(max_length=32,verbose_name="名称")
    password=models.CharField(max_length=32,verbose_name="密码")

class Order(models.Model):
    '''订单管理'''
    name=models.CharField(verbose_name="订单名",max_length=64)
    datatime=models.DateField(verbose_name="婚礼日期")
    phone=models.CharField(verbose_name="联系人电话",max_length=64)
    address=models.CharField(max_length=64,verbose_name="婚礼地址")
    oid=models.CharField(verbose_name="订单号",max_length=64)
    status=(
        (0,"待支付"),
        (1,"已支付")
    )
    status_choice=models.SmallIntegerField(default=0,verbose_name="支付状态",choices=status)
    level=(
        (0,"普通客户"),
        (1,"vip客户")
    )
    level_choice=models.SmallIntegerField(default=0,verbose_name="级别",choices=level)

