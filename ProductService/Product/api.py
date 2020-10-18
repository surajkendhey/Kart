from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
from django.core import serializers
from datetime import datetime
from . import models
from django.db.models import Q


@api_view(['GET'])
def get_products(request):
    product = models.Product.objects.all()
    data = serializers.serialize("json", product)
    return Response(json.loads(data), status=status.HTTP_200_OK)


@api_view(['GET'])
def get_product_by_id_or_name(request, category='', product_id='', product_name=''):

    if 'product_name' in request.GET and 'product_id' in request.GET:
        product_name = request.GET.get('product_name')
        product_id = request.GET.get('product_id')
        query = Q(product_name=product_name) & Q(productid=product_id)
    elif 'product_name' in request.GET:
        product_name = request.GET.get('product_name')
        query = Q(product_name=product_name)
    elif 'product_id' in request.GET:
        product_id = request.GET.get('product_id')
        query = Q(productid=product_id)
    else:
        return Response("Please provide at least one parameter", status=status.HTTP_400_BAD_REQUEST)
    product = models.Product.objects.filter(query)
    data = serializers.serialize("json", product)
    return Response(json.loads(data), status=status.HTTP_200_OK)


@api_view(['GET'])
def get_product_by_category(request, category=''):
    if 'category' in request.GET:
        category = request.GET.get('category')
        categories = category.split(',')
        print(categories)
        query = Q(category__category_name__in=categories)
    else:
        return Response("Please provide at least one parameter", status=status.HTTP_400_BAD_REQUEST)
    product = models.Product.objects.filter(query)
    data = serializers.serialize("json", product)
    return Response(json.loads(data), status=status.HTTP_200_OK)


@api_view(['POST'])
def create_category(request):
    category_name = request.data['name']
    category_id = request.data['id']

    category = models.Category(categoryid=category_id, category_name=category_name.lower(),date_posted=datetime.now())
    try:
        category.save()
    except Exception as e:
        return Response("Unable to save the category information:"+e,status=status.HTTP_400_BAD_REQUEST)

    return Response("Category created successfully", status=status.HTTP_200_OK)

@api_view(['POST'])
def create_product(request):
    product_name = request.data['name']
    description = request.data['description']
    product_id = request.data['id']
    categories = request.data['category']
    vendor = request.data["vendor"]
    print(categories)
    categoryObj= models.Category.objects.filter(category_name__in=categories)
    print("AAAA: "+str(len(categoryObj)))

    product = models.Product(product_name=product_name,productid=product_id,description=description,
                             vendor=vendor)
    try:
        product.save()
        if len(categoryObj) > 0:
            product.category.add(*categoryObj)
    except Exception as e:
        print(e)
        return Response("Unable to save the Product information: "+str(e),status=status.HTTP_400_BAD_REQUEST)

    return Response("Product created successfully", status=status.HTTP_200_OK)
