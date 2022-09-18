from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path('',views.productList, name = 'product_list'),
    path('<slug:slug>/', views.productList, name = 'product_list_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
               ]