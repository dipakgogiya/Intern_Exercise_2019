class Inventory_Management:
	def __init__(self,product_detail):
		self.product_detail = product_detail
	def purchase(self,product_quantity,product_price):
		"""
		@Func : It can manage the purchase of product and it's quantity
		@Param1 : product_quantity is the total quantity of the product and it's type is integer
		@Param2 : product_price is the total price of the product quantities and it's type is integer
		@Return : It can return the total product detail in dictinary
		"""	
		if self.product_detail == 0:
			self.product_detail = {1:{'product_qty':product_quantity,'product_price':product_price}}
		else:
				self.product_detail.update({self.product_detail.keys()[-1]+1:{'product_qty':product_quantity,'product_price':product_price}})
				print(self.product_detail.values()[0]['product_qty'])
		return self.product_detail

	def sales(self,product_quantity):
		"""
		@Func : It can manage the sales of product by the product quantity
		@Param1 : product_quantity is the total quantity of the product you want to sale and it's type is integer
		@Return : It can return the updated total product detail in dictionary
		"""
		for i in [self.product_detail.items()]:
			print(i)
			if product_quantity <= i[0][1]['product_qty']:
				i[0][1]['product_qty'] -= product_quantity
				if i[0][1]['product_qty'] == 0:
					del self.product_detail[self.product_detail.keys()[0]]	
			else:
				product_quantity = product_quantity - i[0][1]['product_qty']
				del self.product_detail[self.product_detail.keys()[0]]
				return self.sales(product_quantity)
		return self.product_detail
		
	def valuation(self):
		"""
		@Func : It can valuation of the final quantity and price and display it final average
		@Return : It can return the total average
		"""
		x = []
		y = []
		for j in self.product_detail:
			x.append(self.product_detail[j]['product_price'])
			y.append(self.product_detail[j]['product_qty'])
			total_price = sum(x)
			total_quantity = sum(y)
			total_average = total_price / total_quantity
		return total_average		
		
product_object = Inventory_Management(0)

print("1. Purchase Product:")
print("2. Product Sale:")
print("3. Valuation:")
print("4. Exit:")

while(True):
	number = int(input("Enter The Number You Want To Perform Given Operation:"))
	if number == 1:
		product_quantity = raw_input("Enter The Product Quantity:")
		product_price = raw_input("Enter The Product Price:")
		if product_quantity.isalpha() or product_price.isalpha():
			print("Enter The Positive Number:")
			exit()
		else:
			product_quantity = int(product_quantity)
			product_price = int(product_price)
			product_info = product_object.purchase(product_quantity,product_price)
			print(product_info)
	elif number == 2:
		product_quantity = int(input("Enter The Product Sale Quantity:"))
		product_info = product_object.sales(product_quantity)
		print(product_info)
	elif number == 3:
		average = product_object.valuation()
		print("Remaining Average Is:",average)
	elif number == 4:
		exit()
	else:
		print("Something is Wrong.Please Try Again.")
