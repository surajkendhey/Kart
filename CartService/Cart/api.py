from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . import models

'''''
@api_view(['POST'])
def create_cart(request, product_id='', product_name='', quantity=0):
    product_id = request.data['product_id']
    product_name = request.data['product_name']
    quantity = request.data['quantity']
    categoryObj = models.Category.objects.filter(category_name__in=categories)
    print("AAAA: " + str(len(categoryObj)))

    product = models.Product(product_name=product_name, productid=product_id, description=description,
                             vendor=vendor)
    try:
        product.save()
        if len(categoryObj) > 0:
            product.category.add(*categoryObj)
    except Exception as e:
        print(e)
        return Response("Unable to save the Product information: " + str(e), status=status.HTTP_400_BAD_REQUEST)
    return Response("Product created successfully", status=status.HTTP_200_OK)
'''''