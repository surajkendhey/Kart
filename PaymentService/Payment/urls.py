
from . import views
from . import api
from django.urls import path

urlpatterns = [
#    path('', views.index, name='index'),
    path('makePayment/', api.make_payment, name='make_payment'),

]