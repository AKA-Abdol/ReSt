from django.urls import path
from . import views

urlpatterns = [
    path('filter/', views.get_below_price, name='price_filter'),
    path('all/', views.product_list_view, name='list'),
    path('test/', views.test, name='test'),
    path('add/', views.add_product, name='add'),
    path('detail/<int:pk>', views.product_detail_view, name='detail'),
    path('create/', views.product_create_view, name='create')
]
