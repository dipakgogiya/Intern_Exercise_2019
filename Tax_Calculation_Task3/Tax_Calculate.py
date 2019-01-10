class c_gst(object):
	def get_tax(self,product_sale_price):
		"""
		@Func = It Calculate the central GST on base price by 18%
		@Param = the product_sale_price is the price of the product you want to sale and it's type is integer
		@Return = It can return the product_sale_price after calculating the centeral GSTs
		"""
		product_sale_price = product_sale_price * 0.18
		return product_sale_price

class s_gst(c_gst):
	def get_tax(self,product_sale_price):
		"""
		@Func = It Calculate the state tax on the product sale price by 12%
		@Param1 = The product_sale_price is the price of the product you want to sale and it's type is integer
		@Return = It can return the calculated state tax and also return the calculated center GST
		"""
		center_tax_calculate = super(s_gst,self).get_tax(product_sale_price)
		tax_calculate = product_sale_price * 0.12
		return tax_calculate,center_tax_calculate

class Sales(s_gst):
	def Sale(self,product_sale_price):
		"""
		@Func = It Manage the get_tax() method
		@Param1 = The product_sale_price is the price of the product you want to sale and it's type is integer
		@Return = It can return the final amount,state tax and center GST return by the get_tax() method
		"""
		a,b,c = self.get_tax(product_sale_price)
		return a,b,c
	def get_tax(self,product_sale_price):
		"""
		@Func = It calculate total/final amount after the calculating state tax and central GST with the product sale price
		@Param1 = The product_sale_price is the price of the product you want to sale and it's type is integer
		@Return = It can return the final amount,state tax and center GST
		"""
		state_tax_calculate = super(Sales,self).get_tax(product_sale_price)
		final_amount = product_sale_price + state_tax_calculate[0] + state_tax_calculate[1]
		return final_amount,state_tax_calculate[0],state_tax_calculate[1]

product_sale_price = raw_input("Enter The Producrt Sale Price:")
if product_sale_price.isalpha():
	print("Please enter the Positive Number:")
else:
	product_sale_price = int(product_sale_price)
	sale = Sales().Sale(product_sale_price)
	print("The Center Gst Is:",sale[2])
	print("The State Tax Is:",sale[1])
	print("Final amount is:",sale[0])
	
