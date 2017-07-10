# -*- coding: utf-8 -*-
#
from django.db import models

# Create your models here.



class UserModel(models.Model):
    """docstring for UserModel"""
    # def __init__(self, arg):
    #     super(UserModel, self).__init__()
    #     self.arg = arg
    name = models.CharField(verbose_name='用户名', max_length=254)
    phone = models.CharField(verbose_name='手机号', max_length=254)
    premium = models.CharField(verbose_name='会员', max_length=254)
    fee = models.CharField(verbose_name='付费金额', max_length=254)
    phone_district = models.CharField(verbose_name='手机号所在地', max_length=254)


    def __str__(self):
        return self.name
    class Meta(object):
        """docstring for Meta"""
        def __init__(self, arg):
            super(Meta, self).__init__()
            self.arg = arg

        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = '网站用户'




class ProfileModel(models.Model):
    """docstring for ProfileModel"""
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    district = models.CharField(verbose_name='地区', max_length=254)
    score = models.CharField(verbose_name='分数', max_length=254)
    chg_times = models.CharField(verbose_name='修改次数', max_length=254)


    def __str__(self):
        return ''


    class Meta(object):
        """docstring for Meta"""
        def __init__(self, arg):
            super(Meta, self).__init__()
            self.arg = arg

        db_table = 'profiles'
        verbose_name = '用户其它信息'
