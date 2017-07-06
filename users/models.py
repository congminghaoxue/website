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

    class Meta(object):
        """docstring for Meta"""
        def __init__(self, arg):
            super(Meta, self).__init__()
            self.arg = arg

        db_table = 'users'
        verbose_name = '用户信息统计'
        verbose_name_plural = '用户信息统计'




class ProfileModel(models.Model):
    """docstring for ProfileModel"""
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    district = models.CharField(verbose_name='地区', max_length=254)
    class Meta(object):
        """docstring for Meta"""
        def __init__(self, arg):
            super(Meta, self).__init__()
            self.arg = arg

        db_table = 'profiles'
