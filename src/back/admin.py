from django.contrib import admin
from .models import Category, Image, OrderState, UserInfo, Product, ProductCategory, ProductOrder, ProductSize, Rol, SizeProduct, Stock, Type, UserRol, OrderUser

# Register your models here.
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(OrderState)
admin.site.register(UserInfo)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductOrder)
admin.site.register(ProductSize)
admin.site.register(Rol)
admin.site.register(SizeProduct)
admin.site.register(Stock)
admin.site.register(Type)
admin.site.register(UserRol)
admin.site.register(OrderUser)

