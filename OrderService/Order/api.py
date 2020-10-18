from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime
from . import models


@api_view(['POST'])
def create_order(request):
    """
    {
	"user_id": "1",
	"product_details": [
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
	],
	"payment_details": [
		{
			"reference_number": "qdwd1",
			"mode_of_payment": "cash on delivery",
			"total_amount": 1234
		}
	]
}
    """
    product_details = request.data['product_details']
    payment_details = request.data['payment_details']
    order_date = datetime.now()
    user_id = request.data['user_id']
    total_price = 0
    for product in product_details:
        total_price += product['price']

    order = models.Order(userid=user_id, product_details=product_details, order_date=order_date,
                         total_price=total_price, payment_details=payment_details)
    try:
        order.save()
    except Exception as e:
        print(e)
        return Response("Unable to save the Cart information: " + str(e), status=status.HTTP_400_BAD_REQUEST)
    return Response("Order created successfully with order ID: "+str(order.id), status=status.HTTP_200_OK)