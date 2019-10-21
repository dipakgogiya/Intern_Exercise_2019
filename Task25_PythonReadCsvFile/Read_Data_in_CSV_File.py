import csv
from _csv import reader

path = "import_sale_order_Final.xlsx"
read_file = open(path)
csv_data_read = reader(read_file)

#This is usefull to skip first line of the header
#header = next(csv_data_read) # The first line in the header

csv_data = [row for row in csv_data_read] 
print csv_data
first_list = []
second_list = []
for data in csv_data:
    # header = ['INVOICE TO', 'CUSTOMER ID', 'SUPPLIER_REF_SKU', 'QTY', 'NAME', 'ADDRESS', 'ADDRESS 2', 'ZIPCODE', 'CITY', 'COUNTRY', 'REFERENCE']
	print data
	first_list.append(data[0])
	second_list.append(data[1])

print first_list
print second_list
 


#['STARCD173501', 'STARCF182801', '7PLUSF173202', '7PLUSF174501', 'MALTAE150301', 'ASTN180501']
