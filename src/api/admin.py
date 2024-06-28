from django.contrib import admin
from api.models import Category,  OrderState, Product, ProductCategory, OrderItem, ProductSize, Size, Stock, Type, OrderUser, Review, Image

# Register your models here.
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(OrderState)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(OrderItem)
admin.site.register(ProductSize)
admin.site.register(Size)
admin.site.register(Stock)
admin.site.register(Type)
admin.site.register(OrderUser)
admin.site.register(Review)

