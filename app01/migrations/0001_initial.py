# Generated by Django 4.0.2 on 2022-06-03 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminname', models.CharField(max_length=32, verbose_name='名称')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='Depart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='职务名称')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='数量')),
                ('wine', models.CharField(max_length=64, verbose_name='酒种')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格')),
                ('wine_type', models.SmallIntegerField(choices=[(0, '500'), (1, '800'), (2, '1000'), (3, '1200')], default=1, verbose_name='类型')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='订单名')),
                ('datatime', models.DateField(verbose_name='婚礼日期')),
                ('phone', models.CharField(max_length=64, verbose_name='联系人电话')),
                ('address', models.CharField(max_length=64, verbose_name='婚礼地址')),
                ('oid', models.CharField(max_length=64, verbose_name='订单号')),
                ('status_choice', models.SmallIntegerField(choices=[(0, '待支付'), (1, '已支付')], default=0, verbose_name='支付状态')),
                ('level_choice', models.SmallIntegerField(choices=[(0, '普通客户'), (1, 'vip客户')], default=0, verbose_name='级别')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='数量')),
                ('typeCar', models.CharField(max_length=32, verbose_name='品牌')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格')),
                ('status_choice', models.SmallIntegerField(choices=[(0, '已占用'), (1, '待占用')], default=1, verbose_name='状态')),
                ('colour', models.CharField(max_length=32, verbose_name='颜色')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='姓名')),
                ('gender', models.SmallIntegerField(choices=[(0, '男'), (1, '女')], default=0, verbose_name='性别')),
                ('phone', models.CharField(max_length=64, verbose_name='电话')),
                ('address', models.CharField(max_length=64, verbose_name='地址')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('photo', models.FileField(max_length=128, upload_to='photo/', verbose_name='照片')),
                ('cancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.depart', verbose_name='职务')),
            ],
        ),
    ]
