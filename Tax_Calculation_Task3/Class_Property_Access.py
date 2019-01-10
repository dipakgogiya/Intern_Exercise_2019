class c_gst(object):
	def get_tax(self,product_sale_price):
		"""
		@Func = It Calculate the central GST on base price by 18%
		@Param = the product_sale_price is the price of the product you want to sale and it's type is integer
		"""
		self.product_sale_price1 = product_sale_price * 0.18

class s_gst(c_gst):
	def get_tax(self,product_sale_price):
		"""
		@Func = It Calculate the state tax on the product sale price by 12%
		@Param1 = The product_sale_price is the price of the product you want to sale and it's type is integer
		"""
		super(s_gst,self).get_tax(product_sale_price)
		self.product_sale_price2 = product_sale_price * 0.12

class Sales(s_gst):
	def Sale(self,product_sale_price):
		"""
		@Func = It Manage the get_tax() method
		@Param1 = The product_sale_price is the price of the product you want to sale and it's type is integer
		@Return = It can return the final amount,state tax and centeral GST return 
		"""
		self.get_tax(product_sale_price)
		return product_sale_price + self.product_sale_price1 + 								self.product_sale_price2,self.product_sale_price1,self.product_sale_price2
		
	def get_tax(self,product_sale_price):
		"""
		@Func = It Calculate the state tax on the product sale price
		@Param1 = The product_sale_price is the price of the product you want to sale and it's type is integer
		"""
		super(Sales,self).get_tax(product_sale_price)
		
		
product_sale_price = raw_input("Enter The Producrt Sale Price:")
if product_sale_price.isalpha():
	print("Please enter the Positive Number:")
else:
	product_sale_price = int(product_sale_price)
	sale = Sales().Sale(product_sale_price)
	print("The State Tax Is:",sale[2])
	print("The Center GST Is:",sale[1])
	print("Final amount is:",sale[0])
	
