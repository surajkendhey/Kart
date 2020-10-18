
from . import views
from . import api
from django.urls import path

urlpatterns = [
#    path('', views.index, name='index'),
    path('getProduct/', api.get_products, name='get_products'),
]