
from . import views
from . import api
from django.urls import path, re_path
from django.conf.urls import url

urlpatterns = [
#    path('', views.index, name='index'),
    path('getProduct/', api.get_products, name='get_products'),
    path('createProduct', api.create_product, name='create_product'),
    path('createCategory', api.create_category, name='create_category'),
    #re_path('getProductById?productID=$', api.get_product_by_id, name='get_product_by_id'),
    #re_path(r'^getProductById(?P<productID>\D+)/',api.get_product_by_id, name='get_product_by_id'),
    #re_path(r'^getProductById/(?P<productID>)', api.get_product_by_id),
    re_path(r'^getProductById/(?P<product_id>)(?P<product_name>)', api.get_product_by_id_or_name),
    re_path(r'^getProductByCategory/(?P<category>)', api.get_product_by_category),


]