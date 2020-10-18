
from . import views
from . import api
from django.urls import path

urlpatterns = [
#    path('', views.index, name='index'),
    path('createOrder/', api.create_order, name='create_order'),
]