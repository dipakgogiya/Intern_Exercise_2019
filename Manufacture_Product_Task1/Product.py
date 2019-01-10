class Manufacture_Product:
	def __init__(self,row_Material,row_Material_Quantity):
		"""
		Functionality = __init__() method is initialize all The Attributes
		Param1 = row_Material is a name of row material and it's type is string
		Param2 = row_Material_Quantity is a quantity of raw material and it's type is integer
		"""
		self.row_Material = row_Material
		self.row_Material_Quantity = row_Material_Quantity

	def purchase_Product(self,purchase_row_Material):
		"""
		Functionality = purchase_Product() Method is used to Manage a Product Purchase
		Param1 = purchase_row_Material is a quantity of total product of row material
		Return = It Return Total Quantity Of Raw Material After Purchasing
		"""
		self.row_Material_Quantity += purchase_row_Material
		return self.row_Material_Quantity

	def produce(self,product_Row_Material_Quantity):
		"""
		Functionality = Produce Method is Managing a Manufacture Product
		Param1 = product_Row_Material_Quantity is a Quantity Of MAnufacture Product and it's Type is Integer
		Return = Return the Manufacture Product Name And it's Quantity 
		"""
		if product_Row_Material_Quantity > self.row_Material_Quantity:
			print("Remaining Quantity Is:",(product_Row_Material_Quantity-self.row_Material_Quantity))
			
		else:
			self.row_Material_Quantity -= product_Row_Material_Quantity
			return self.row_Material_Quantity

	def getStock(self):
		"""
		Functionality = getStock() method display the current stock
		Param1 = row_material_quantity is a Total Or Remaining quantity of row_material
		Return = It return the row_Material Quantity
		"""
		return self.row_Material_Quantity


row_Material = raw_input("Enter Row Material:")
row_Material_Quantity = int(input("Enter Row Material Quantity:"))

product_object = Manufacture_Product(row_Material,row_Material_Quantity)

print("1. Purchase The Product:")
print("2. Produce The Product:")
print("3. Get Current Stock:")
print("4. Exit")
while(True):
	number = int(input("Enter The Number To Perform Given Operation:= "))
	if number == 1:
		purchase_row_Material = int(input("Purchase The Quantity of Raw Material:"))
		Quantity = product_object.purchase_Product(purchase_row_Material)
		print("Total Quantity Of Raw Material",Quantity)
	elif number == 2:
		product_Row_Material_Quantity = int(input("Enter Product Row Material Quantity:"))
		Quantity = product_object.produce(product_Row_Material_Quantity)
		print("Quantity Is:",Quantity)
	elif number == 3:
		quantity_stock = product_object.getStock()
		print("Current Stock Is:",quantity_stock)
	elif number == 4:
		exit()
	else:
		print("Print Enter The Number:")
