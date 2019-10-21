from SaleProduct import *
from PurchaseProduct import *
import xlwt
import xlrd
from xlutils.copy import copy
#xlutils package collects utilities that require both xlrd and xlwt, including the ability to copy and modify or filter existing excel files.
class Product(PurchaseProduct,SaleProduct):
	product_detail = dict()
	def __init__(self,productName,productType):
		"""	
		@Func :- It can initialize all the properties
		@Param1 :- productName is the name of the product name and it's type is string
		@Param2 :- productType is the type of the product and it's type is string
		"""
		#Workbook() is used to create a wrokbook
		work_book = xlwt.Workbook()
		#add_sheet is used to create a sheet
		purchase_sheet = work_book.add_sheet("purchase_sheet")
		sale_sheet = work_book.add_sheet("sale_sheet")
		product_sheet = work_book.add_sheet("product_sheet")
		
		style = xlwt.easyxf('pattern: pattern solid, fore_colour light_blue;''font: colour white, bold True;') 
		header_lists = ['Order-Number', 'Date', 'Quantity', 'Vendor-Name', 'Basic-Price', 'Total-Price', 'Total-Tax']
		product_lists = ['Product-Name','Product-Type','Purchase-Order-Number', 'Sale-Order-Number','Available-Quantity','Total-Profit']
		for i in range(0,len(header_lists)):
			purchase_sheet.write(0,i,header_lists[i],style)  #Write the header in purchase_sheet
			sale_sheet.write(0,i,header_lists[i],style) #Write the header in sale_sheet
		for i in range(0,len(product_lists)):	
			product_sheet.write(0,i,product_lists[i],style)
		#save() method is used to save and commit the data into file
		work_book.save('product.xls')
		
		self.productName = productName
		self.productType = productType
		self.product_detail[self.productName] = {"productname":self.productName,"producttype":self.productType,"availablequantity":0,"purchaseordernumber":False,"saleordernumber":0,"totalprofit":0}
		
	def write_data_excel(self,Dictionary_Data,sheet,work_book):
		"""
		@Func :- It will manage the excel sheets 
		@Param1 :- Dictionary_Data is a dictionary and it's type is dict
		@Param2 :- sheet is the name of sheet which is type is object
		@Param3 :- work_book is the name of work book and it's type is object
		"""
		for row in range(1,len(Dictionary_Data)+1):
			sheet.write(row,0,Dictionary_Data[row]['ordernumber'])
			sheet.write(row,1,Dictionary_Data[row]['date'])
			sheet.write(row,2,Dictionary_Data[row]['qty'])
			sheet.write(row,3,Dictionary_Data[row]['vendorname'])
			sheet.write(row,4,Dictionary_Data[row]['basicprice'])
			sheet.write(row,5,Dictionary_Data[row]['totalprice'])
			sheet.write(row,6,Dictionary_Data[row]['totaltax'])
			work_book.save('product.xls')# It is used to save and commit the data into file
			
	def write_product_data_excel(self,sheet,work_book):
		"""
		@Func :- It will manage the excel product sheets 
		@Param1 :- sheet is the name of sheet which is type is object
		@Param2 :- work_book is the name of work book and it's type is object
		"""
		for row in range(1,len(self.product_detail)+1):
			sheet.write(row,0,self.product_detail[self.productName]['productname'])
			sheet.write(row,1,self.product_detail[self.productName]['producttype'])
			sheet.write(row,2,",".join(self.product_detail[self.productName]['purchaseordernumber']))
			if self.product_detail[self.productName]['saleordernumber'] == False:
				sheet.write(row,3,self.product_detail[self.productName]['saleordernumber'])
			else:
				sheet.write(row,3,",".join(self.product_detail[self.productName]['saleordernumber']))
			sheet.write(row,4,self.product_detail[self.productName]['availablequantity'])
			sheet.write(row,5,self.product_detail[self.productName]['totalprofit'])
			work_book.save('product.xls')
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
		self.product_detail[self.productName]['availablequantity'] += self.purchase_product_detail.items()[-1][1]['qty']
		#self.product_detail[1]['availablequantity'] += purchaseProductQuantity
		purchase_order_number = []
		for purchase_info in range(1,len(self.purchase_product_detail)+1):
			purchase_order_number.append(self.purchase_product_detail[purchase_info]['ordernumber']) 
			self.product_detail[self.productName]['purchaseordernumber'] = purchase_order_number
		read_book = xlrd.open_workbook("product.xls")#xlrd.open_workbook() is used to read the data into a excel file
		work_book = copy(read_book) #It is used to copy the read_book object
		
		purchase_sheet = work_book.get_sheet(0) #It is used to get the sheet name
		#purchase_sheet.write(0,i,self.purchase_product_detail[i].keys()[i])
		self.write_data_excel(self.purchase_product_detail, purchase_sheet,work_book)#It is used to write data into excel file in purchase-sheet
		product_sheet = work_book.get_sheet(2)
		self.write_product_data_excel(product_sheet,work_book)
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
		self.product_detail[self.productName]['availablequantity'] -= self.sale_product_detail.items()[-1][1]['qty']
		total_profit = 0
		total_loss = 0
		total_purchase = self.purchase_product_detail.items()[-1][1]['basicprice'] * saleQuantity
		total_sale = saleQuantity * saleBasicPrice
		if total_sale > total_purchase:
			total_profit = total_sale - total_purchase
			self.product_detail[self.productName]['totalprofit'] += total_profit
		else:
			total_loss = total_purchase - total_sale
			self.product_detail[self.productName]['totalprofit'] -= total_loss	
			
		sale_order_number = []
		for sale_info in range(1,len(self.sale_product_detail)+1):
			sale_order_number.append(self.sale_product_detail[sale_info]['ordernumber'])
			self.product_detail[self.productName]['saleordernumber'] = sale_order_number
		read_book = xlrd.open_workbook("product.xls") #xlrd.open_workbook() is used to read the data into a excel file
		work_book = copy(read_book)#It is used to copy the read_book object
		
		sale_sheet = work_book.get_sheet(1) #It is used to get the sheet name
		
		self.write_data_excel(self.sale_product_detail, sale_sheet,work_book) #It is used to write data into excel file in sales-sheet
		product_sheet = work_book.get_sheet(2)
		self.write_product_data_excel(product_sheet,work_book)
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
	
