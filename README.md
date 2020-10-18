# Kart



Microservices architecture is used here so all of the services are independent of each other.
Each service is having its own DB,
Service can orcestrate using a common Dashboard.controller (Not implemented yet)

Note:
1. Business Logic is in api.py file for each service
2. For Architecture please refer the "Hig Level Architecture.jpg" file or https://github.com/surajkendhey/Kart/blob/main/Hig%20Level%20Architecture.jpg
3. For Date models please reder "models.py" file for each service



----------------------------------------------------
Create Product
--------------------------------------------------
URL : http://127.0.0.1:8000/Product/createProduct/

Header: content-type = application/json

Body: 
{
"name": "Nike Laced up shoe",
"description": "White shoes",
"id": "AYADFG134",
"category": ["Men", "Shoes"],
"vendor": "SK Traders"
}

---------------------------------------------------
Get Product by Name or ID
---------------------------------------------------
url: http://127.0.0.1:8000/Product/getProductById?productID=AYADFG134

Response:
[{
  "model": "Product.product",
  "pk": 8,
  "fields": {
    "productid": "AYADFG134",
    "product_name": "Nike Laced up shoe",
    "description": "White shoes",
    "image": "",
    "quantity": 0,
    "regular_price": "0.00",
    "discounted_price": "0.00",
    "product_rating": "0.00",
    "product_review": "0.00",
    "vendor": "SK Traders",
    "category": [3, 4]
  }
}]

-----------------------------------------------------
GET PRODUCT BY CATEGORY
------------------------------------------------------
url: http://127.0.0.1:8000/Product/getProductByCategory?category=Men,shoes

Response: 

[{
  "model": "Product.product",
  "pk": 6,
  "fields": {
    "productid": "NIKETS126",
    "product_name": "nike t shirt",
    "description": "Nike t",
    "image": "",
    "quantity": 0,
    "regular_price": "0.00",
    "discounted_price": "0.00",
    "product_rating": "0.00",
    "product_review": "0.00",
    "vendor": "",
    "category": [3, 4]
  }
}, {
  "model": "Product.product",
  "pk": 7,
  "fields": {
    "productid": "NIKETS127",
    "product_name": "nike t shirt",
    "description": "Nike t",
    "image": "",
    "quantity": 0,
    "regular_price": "0.00",
    "discounted_price": "0.00",
    "product_rating": "0.00",
    "product_review": "0.00",
    "vendor": "iscon",
    "category": [3, 4]
  }
}, {
  "model": "Product.product",
  "pk": 8,
  "fields": {
    "productid": "AYADFG134",
    "product_name": "Nike Laced up shoe",
    "description": "White shoes",
    "image": "",
    "quantity": 0,
    "regular_price": "0.00",
    "discounted_price": "0.00",
    "product_rating": "0.00",
    "product_review": "0.00",
    "vendor": "SK Traders",
    "category": [3, 4]
  }
}]

---------------------------------------------------
CREATE CATEGORY
----------------------------------------------------
URL: http://127.0.0.1:8000/Product/createCategory
Method: POST
Body:
{
"name": "women",
"id": "women"
}

Response: "Category created successfully"


----------------------------------------------------
Create Cart
----------------------------------------------------

URL: http://127.0.0.1:8001/Cart/addToCart/

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
	]
}
--------------------------------------------------
Create Order
--------------------------------------------------

URL: http://127.0.0.1:8002/Order/createOrder/

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

----------------------------------------------------
Make Payment
-------------------------------------------------------
url: http://127.0.0.1:8004/Payment/makePayment/

{
	"payment_gateway": "payTM",
	"payment_type": "DEBITCARD",
	"amount": 3000,
	"orderid": 1,
	"userid": 1
}


Response: "Payment successfull with reference no:  C2EEC0"
