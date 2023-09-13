from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255, blank=True ,null=True)
    phone_number = models.CharField(max_length=20, blank=True ,null=True)
    age = models.IntegerField(blank=True ,null=True)
    gender = models.CharField(max_length=10, blank=True ,null=True)
    address = models.CharField(max_length=200, blank=True ,null=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'customer'
        verbose_name_plural = '고객(customer)'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    img_path = models.CharField(max_length=255, blank=True ,null=True)
    category = models.CharField(max_length=255, null=True)
    price = models.IntegerField()
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'
        verbose_name_plural = '상품(product)'
    
    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id',)
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id',)
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'
        verbose_name_plural = '주문(orders)'


class Order01(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id',)
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id',)
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders01'
        verbose_name_plural = '주문(orders01)'

class Order02(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id',)
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id',)
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders02'
        verbose_name_plural = '주문(orders02)'


# Order03 모델
class Order03(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders03'
        verbose_name_plural = '주문(orders03)'

# Order04 모델
class Order04(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders04'
        verbose_name_plural = '주문(orders04)'

# Order05 모델
class Order05(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders05'
        verbose_name_plural = '주문(orders05)'

# Order06 모델
class Order06(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders06'
        verbose_name_plural = '주문(orders06)'

# Order07 모델
class Order07(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders07'
        verbose_name_plural = '주문(orders07)'

# Order08 모델
class Order08(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders08'
        verbose_name_plural = '주문(orders08)'

# Order09 모델
class Order09(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders09'
        verbose_name_plural = '주문(orders09)'

# Order10 모델
class Order10(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders10'
        verbose_name_plural = '주문(orders10)'

# Order11 모델
class Order11(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders11'
        verbose_name_plural = '주문(orders11)'

# Order12 모델
class Order12(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders12'
        verbose_name_plural = '주문(orders12)'

# Order13 모델
class Order13(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders13'
        verbose_name_plural = '주문(orders13)'

# Order14 모델
class Order14(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders14'
        verbose_name_plural = '주문(orders14)'

# Order15 모델
class Order15(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders15'
        verbose_name_plural = '주문(orders15)'

# Order16 모델
class Order16(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders16'
        verbose_name_plural = '주문(orders16)'

# Order17 모델
class Order17(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders17'
        verbose_name_plural = '주문(orders17)'

# Order18 모델
class Order18(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders18'
        verbose_name_plural = '주문(orders18)'

# Order19 모델
class Order19(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders19'
        verbose_name_plural = '주문(orders19)'

# Order20 모델
class Order20(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='cust_id')
    prd_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='prd_id')
    promo_id = models.CharField(max_length=255, blank=True, null=True)
    order_cnt = models.IntegerField()
    order_price = models.IntegerField()
    order_dt = models.CharField(max_length=255)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders20'
        verbose_name_plural = '주문(orders20)'






