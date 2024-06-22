from django.db import models

class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    category = models.CharField(max_length=80, null=False)

    def __str__(self):
        return self.category

    class Meta:
        app_label = 'api'  # Ajusta esto según el nombre real de tu aplicación

        constraints = [
            models.UniqueConstraint(fields=['id_category'], name='category_id_category_un')
        ]

class Image(models.Model):
     id_image = models.AutoField(primary_key=True)
     image = models.BinaryField(null=False)
     product_image = models.ForeignKey('Product', on_delete=models.CASCADE, null=False)

     def __str__(self):
        return f"Image for {self.product_image}"

class OrderState(models.Model):
    id_order_state = models.AutoField(primary_key=True)
    order_state = models.CharField(max_length=80, null=True)

    def __str__(self):
        return self.order_state

class UserInfo(models.Model):   
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, null=False)
    encrypted_password = models.CharField(max_length=80, null=False)
    user_name = models.CharField(max_length=80, null=False)
    email = models.CharField(max_length=80, null=False)
    phone_number = models.CharField(max_length=80)
    user_rol = models.ForeignKey('Rol', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user_name

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=4000, null=False)
    price = models.IntegerField(null=False)
    description = models.TextField(blank=True)
    type_category = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.product_name

class ProductCategory(models.Model):
    category_product = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_category} in {self.category_product}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['category_product_id', 'product_category_id'], name='productcategory_16_pk')
        ]

#Used to be ProductOrder, now its the same conexion but has quantity and primary key to identify how many of that product the user is buying
class OrderItem(models.Model):
    id_order_item = models.AutoField(primary_key=True)
    order_quantity = models.IntegerField(null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_user = models.ForeignKey('OrderUser', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order_quantity} of {self.product} in Order #{self.order_user.id_order}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'order_user'], name='unique_order_item')
        ]

class ProductSize(models.Model):
    product_size = models.ForeignKey(Product, on_delete=models.CASCADE)
    size_product = models.ForeignKey('Size', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_size} - {self.size_product}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product_size_id', 'size_product_id'], name='productsize_pk')
        ]

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=80, null=False)

    def __str__(self):
        return self.rol

class Size(models.Model):
    id_size = models.AutoField(primary_key=True)
    size = models.CharField(max_length=5, null=False)

    def __str__(self):
        return self.size

class Stock(models.Model):
    id_stock = models.AutoField(primary_key=True)
    quantity = models.IntegerField(null=False)
    product_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.quantity} units of {self.product_size}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product_size_id'], name='stock_unique')
        ]

class Type(models.Model):
    id_type = models.AutoField(primary_key=True)
    type = models.CharField(max_length=80, null=False)

    def __str__(self):
        return self.type

class OrderUser(models.Model):
    id_order = models.AutoField(primary_key=True)
    date_order = models.DateField(auto_now_add=True, null=False)
    shipping_price = models.FloatField(null=False)
    total_payment = models.FloatField(null=False)
    address = models.CharField(max_length=80, null=False)
    user = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, null=True)
    order_state = models.ForeignKey(OrderState, on_delete=models.SET_NULL, null=True)
    taxes = models.FloatField(null=False)

    def __str__(self):
        return f"Order #{self.id_order} by {self.user}"


#Review Connects with product and userinfo, Review can only have 1 product and user while product and user can have many reviews
class Review(models.Model):
    id_review = models.AutoField(primary_key=True)
    rating = models.IntegerField(null=False)
    comment = models.CharField(max_length=250, null=True)
    creation_date = models.DateField(auto_now_add=True, null=False)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review for {self.product} by {self.user.user_name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'user'], name='unique_review')
        ]

