from SaleProduct import *
from PurchaseProduct import *

class Product(PurchaseProduct,SaleProduct):
	product_detail = dict()
	def __init__(self,productName,productType):
		"""	
		@Func :- It can initialize all the properties
		@Param1 :- productName is the name of the product name and it's type is string
		@Param2 :- productType is the type of the product and it's type is string
		"""
		self.productName = productName
		self.productType = productType
		self.product_detail[self.productName] = {"productname":self.productName,"producttype":self.productType,"availablequantity":0,"purchaseordernumber":False,"saleordernumber":False,"totalprofit":0}

	def Purchase(self,purchaseProductDate,purchaseProductQuantity,purchaseProductVendorName,purchseProductBasicPrice,purchaseProductTotalPrice):
		"""
		@Func :- It will manage the Purchase Product 
		@Param1 :- purchaseProductDate is the product purchase date and it's type is string
		@Param2 :- purchaseProductQuantity is the total purchase product quantity and it's type is integer
		@Param3 :- purchaseProductVendorName is the name of the customer and it's type is string
		@Param4 :- purchseProductBasicPrice is the Basic Price and it's type integer
		@Param5 :- purchaseProductTotalPrice is the Total Product Price and it's type is integer
		@Return :- It will return the total purchase product detail 
		"""
		super(Product,self).purchase_product(purchaseProductDate,purchaseProductQuantity,purchaseProductVendorName,purchseProductBasicPrice,purchaseProductTotalPrice) 
		self.product_detail[self.productName]['availablequantity'] += self.purchase_product_detail.items()[-1][1]['productqty']
		#self.product_detail[1]['availablequantity'] += purchaseProductQuantity
		purchase_order_number = []
		for purchase_info in range(1,len(self.purchase_product_detail)+1):
			purchase_order_number.append(self.purchase_product_detail[purchase_info]['purchaseordernumber']) 
			self.product_detail[self.productName]['purchaseordernumber'] = purchase_order_number
		return self.product_detail

	def Sale(self,saleProductDate,saleQuantity,saleVendorName,saleBasicPrice,saleTotalPrice):
		"""
		@Func :- It will manage the Sale Product 
		@Param1 :- saleProductDate is the product sale date and it's type is string
		@Param2 :- saleQuantity is the total sale product quantity and it's type is integer
		@Param3 :- saleVendorName is the name of the vendor and it's type is string
		@Param4 :- saleBasicPrice is the sale Basic Price and it's type integer
		@Param5 :- saleTotalPrice is the Total sale Price and it's type is integer
		@Return :- It will return the total sale product detail
		"""
		Type = self.product_detail[self.productName]['producttype']
		super(Product,self).sale_product(saleProductDate,saleQuantity,saleVendorName,saleBasicPrice,saleTotalPrice,Type)
		self.product_detail[self.productName]['availablequantity'] -= self.sale_product_detail.items()[-1][1]['saleqty']
		total_profit = 0
		total_loss = 0
		total_purchase = self.purchase_product_detail.items()[-1][1]['purchasebasicprice'] * saleQuantity
		total_sale = saleQuantity * saleBasicPrice
		if total_sale > total_purchase:
			total_profit = total_sale - total_purchase
			self.product_detail[self.productName]['totalprofit'] += total_profit
		else:
			total_loss = total_purchase - total_sale
			self.product_detail[self.productName]['totalprofit'] -= total_loss	
			
		sale_order_number = []
		for sale_info in range(1,len(self.sale_product_detail)+1):
			sale_order_number.append(self.sale_product_detail[sale_info]['saleordernumber'])
			self.product_detail[self.productName]['saleordernumber'] = sale_order_number
		return self.product_detail

productName = raw_input("Enter The Product Name:")
print("Enter The Product Type 'consumable' or 'stock' or 'service' ")
productType = raw_input("Enter The Product_Type:")	
if productType == 'consumable' or productType == 'stock' or productType == 'service':
	product_object = Product(productName,productType)
else:
	print("Please Enter The Right Product Type below")
	exit()
print("1.Purchase The Product:")
print("2.Sale The Product:")
print("3.Exit:")
while(True):
	number = int(input("Enter The Number Given In The Operation:"))
	if number == 1:
		purchaseProductDate = datetime.datetime.now().strftime("%Y/%m/%d")
        	purchaseProductQuantity = int(input("Enter The Purchase Product Quantity:"))
        	purchaseProductVendorName = raw_input("Enter The Vendor Name:")
        	purchseProductBasicPrice = int(input("Enter The Basic Quantity Price:"))
        	purchaseProductTotalPrice = purchseProductBasicPrice * purchaseProductQuantity
		purchase_detail = product_object.Purchase(purchaseProductDate,purchaseProductQuantity,purchaseProductVendorName,purchseProductBasicPrice,purchaseProductTotalPrice)
		print(purchase_detail)
	elif number == 2:
		saleProductDate = datetime.datetime.now().strftime("%Y/%m/%d")
        	saleQuantity = int(input("Enter The Product Sale Quantity:"))
        	saleVendorName = raw_input("Enter The Sale Vendor Name:")
        	saleBasicPrice = int(input("Enter The Basic Quantity Price:"))
        	saleTotalPrice = saleBasicPrice * saleQuantity  
		sale_detail = product_object.Sale(saleProductDate,saleQuantity,saleVendorName,saleBasicPrice,saleTotalPrice)
		print(sale_detail)
	elif number == 3:
		exit()
	else:
		print("Something Was Wrong...Please Try Again")
	
