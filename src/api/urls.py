from django.urls import path, include
from rest_framework.routers import DefaultRouter
from EncoraEcommerce.src.api.views.views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'images', ImageViewSet)
router.register(r'order_states', OrderStateViewSet)
router.register(r'users', UserInfoViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product_categories', ProductCategoryViewSet)
router.register(r'product_orders', ProductOrderViewSet)
router.register(r'product_sizes', ProductSizeViewSet)
router.register(r'roles', RolViewSet)
router.register(r'sizes', SizeViewSet)
router.register(r'stocks', StockViewSet)
router.register(r'types', TypeViewSet)
router.register(r'user_roles', UserRolViewSet)
router.register(r'orders', OrderUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
