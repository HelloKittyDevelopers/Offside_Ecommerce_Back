from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.views import *
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'categories', CategoryView, 'categories')
router.register(r'images', ImageView, 'images')
router.register(r'order_states', OrderStateView, 'order_states')
router.register(r'products', ProductView, 'products')
router.register(r'product_categories', ProductCategoryView, 'product_categories')
router.register(r'order_item', OrderItemView, 'order_item')
router.register(r'product_sizes', ProductSizeView, 'product_sizes')
router.register(r'sizes', SizeView, 'sizes')
router.register(r'stocks', StockView, 'stocks')
router.register(r'types', TypeView, 'types')
router.register(r'orders', OrderUserView, 'orders')
router.register(r'reviews', ReviewView, 'reviews')

urlpatterns = [
    path("", include(router.urls)),
    path('docs/', include_docs_urls(title="Home API")),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('type/<str:type>/', ProductListingView.as_view(), name='product-listing')
]
