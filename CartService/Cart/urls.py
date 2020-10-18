
from . import views
from . import api
from django.urls import path

urlpatterns = [
#    path('', views.index, name='index'),
    path('addToCart/', api.create_update_cart, name='create_update_cart'),
]