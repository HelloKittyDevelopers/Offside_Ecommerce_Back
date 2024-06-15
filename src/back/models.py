from django.db import models

# Create your models here.

class Category(models.Model):
    id_category = models.IntegerField(unique=True)
    category = models.CharField(max_length=80)
    category_product_id = models.AutoField(primary_key=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_category'], name='category_id_category_un')
        ]

class Image(models.Model):
    id_image = models.AutoField(primary_key=True)
    image = models.BinaryField()
    product_image = models.ForeignKey('Product', on_delete=models.CASCADE)

class OrderState(models.Model):
    id_order_state = models.AutoField(primary_key=True)
    order_state = models.CharField(max_length=80, null=True)

class UserInfo(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=80)
    encrypted_password = models.CharField(max_length=80)
    user_name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=80, null=True)

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=4000)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    stock = models.IntegerField()
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)

class ProductCategory(models.Model):
    category_product = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['category_product', 'product_category'], name='productcategory_16_pk')
        ]

class ProductOrder(models.Model):
    product_order = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_product = models.ForeignKey('OrderUser', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product_order', 'order_product'], name='productorder_pk')
        ]

class ProductSize(models.Model):
    product_size = models.ForeignKey(Product, on_delete=models.CASCADE)
    size_product = models.ForeignKey('SizeProduct', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product_size', 'size_product'], name='productsize_pk')
        ]

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=80)

class SizeProduct(models.Model):
    id_size = models.AutoField(primary_key=True)
    size_prod = models.CharField(max_length=80)

class Stock(models.Model):
    id_stock = models.AutoField(primary_key=True)
    quantity = models.CharField(max_length=80)
    product_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)

class Type(models.Model):
    id_type = models.AutoField(primary_key=True)
    type = models.CharField(max_length=80)

class UserRol(models.Model):
    user_rol = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    rol_user = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_rol', 'rol_user'], name='usuario_rol_pk')
        ]

class OrderUser(models.Model):
    id_order = models.AutoField(primary_key=True)
    date_order = models.DateField()
    total_payment = models.FloatField()
    address = models.CharField(max_length=80)
    user_user = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, null=True)
    order_state = models.ForeignKey(OrderState, on_delete=models.SET_NULL, null=True)
    taxes = models.FloatField()

