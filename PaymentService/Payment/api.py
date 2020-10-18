from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import uuid
from datetime import datetime
from . import models

@api_view(['GET'])
def get_products(request):
    return Response({"Addidas Shoes", }, status=status.HTTP_200_OK)


@api_view(['POST'])
def make_payment(request):
    payment_gateway = request.data['payment_gateway']
    payment_type = request.data['payment_type']
    amount = request.data['amount']
    account_number = 'dddddddddddddd'
    order_id = request.data['orderid']
    userid = request.data['userid']
    transaction_date = datetime.now()
    Reference_no = uuid.uuid4().hex[:6].upper()
    gateway_response = {"Reference_no": Reference_no, "bank": "hdfc"}

    transaction_obj = models.Transaction(orderid=order_id, userid=userid, transaction_date=transaction_date,
                                         amount=amount, response= gateway_response,
                                         payment_type=payment_type_method(payment_type))
    try:
        transaction_obj.save()
    except Exception as e:
        return Response("Unable to make payment" + str(e), status=status.HTTP_400_BAD_REQUEST)
    return Response("Payment successfull with reference no:  "+str(Reference_no), status=status.HTTP_200_OK)


def payment_type_method(type):
    ptype =  models.PaymentMode.objects.filter(type=type)
    print("tyyy",ptype)
    return ptype[0]