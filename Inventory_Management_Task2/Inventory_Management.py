class Inventory_Management:
	def __init__(self,product_name,product_quantity):
		"""
		@Func = It initialize all the class attributes.
		@Param1 = product_name is a name of the product and it's type is string.
		@Param2 = product_quantity is a total product quantity and it's type is integer.
		@Return = It return product_name and it's total quantity.
		"""
		self.product_name = product_name
		self.product_quantity = product_quantity
	def purchase(self,product_name,product_quantity):
		"""
		@Func = It can manage the purchase product by taking a product name and it's quantity. 
		@param1 = product_name is the name of the product and it's type is string.
		@param2 = product_quantity is the quantity of product you need to purchase and it's type is integer.
		return = It return product name and total quantity after purchase a new quantity.
		"""
		self.product_quantity += product_quantity
		return self.product_name,self.product_quantity

	def sale_Product(self,product_name,product_quantity):
		"""
		@Func = It can manage the product sale by taking a product name and it's quantity.
		@Param1 = product_name is the name of the product and it's type is string.
		@Param2 = product_quantity is the total quantity of the product and it's type is integer.
		@Return = It return product name and remaining quantity after sale the product.
		""" 
		self.product_quantity -= product_quantity
		return self.product_name,self.product_quantity
	def final_Count(self):
		"""
		@Func = It can manage a total product quantity.
		@Return = It return total product quantity.
		"""
		return self.product_quantity

product_name = raw_input("Enter The Name Of Product:")
product_quantity = raw_input("Enter Quantity Of Product:")

if product_quantity.isalpha(): 
	print("Please Enter The Positive Number:")
	exit()
else:
	product_quantity = int(product_quantity)
	product_object = Inventory_Management(product_name,product_quantity)

print("1. Purchase Product:")
print("2. Sale The Product:")
print("3. Final Count Of Product:")
print("4. Exit")

while(True):
	number = int(input("Enter The Number To Perform Given Operation:"))
	if number > 0:	
		if number == 1:
			product_quantity = int(input("Enter Product Quantity:"))
			name,quantity = product_object.purchase(product_object,product_quantity)
			print("Product Name Is:",name)
			print("Total Product Quantity Is:",quantity)
		elif number == 2:
			product_quantity = int(input("Enter The Product Quantity You Want To Sale:"))
			name,quantity = product_object.sale_Product(product_object,product_quantity)
			print("Product Name Is:",name)
			print("The Remaining Quantity Is:",quantity)
		elif number == 3:
			final_quantity = product_object.final_Count()
			print("The Final Quantity is:",final_quantity)
		elif number == 4:
			exit()
		else:
			print("Enter The Number for given in the operation as per your requirement:")
	else:
		print("Please Enter The Positive Number as Quantity and also enter greater then zero (>0) :")
