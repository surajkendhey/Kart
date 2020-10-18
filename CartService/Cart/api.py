from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . import models


@api_view(['POST'])
def create_update_cart(request):
    """
    {
	"user_id": "1",
	"product_details":
	    [
            {
                "product_id": "2",
                "quantity": 1,
                "price": 1000
            },
            {
                "product_id": "3",
                "quantity": 1,
                "price": 1000
            }
	    ]
    }
    """

    product_details = request.data['product_details']
    user_id = request.data['user_id']

    cart = models.Cart(id=1,userid=user_id, product_details=product_details)
    try:
        cart.save()
    except Exception as e:
        print(e)
        return Response("Unable to save the Cart information: " + str(e), status=status.HTTP_400_BAD_REQUEST)
    return Response("Cart created successfully", status=status.HTTP_200_OK)

