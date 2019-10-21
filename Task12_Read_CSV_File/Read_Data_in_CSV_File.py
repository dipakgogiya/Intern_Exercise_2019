import csv
from _csv import reader

path = "/home/emipro/Downloads/import_sale_order_Final.csv"
read_file = open(path)
csv_data_read = reader(read_file)

#This is usefull to skip first line of the header
header = next(csv_data_read) # The first line in the header

csv_data = [row for row in csv_data_read] 

dictionary_data= dict()
for data in csv_data:
    # header = ['INVOICE TO', 'CUSTOMER ID', 'SUPPLIER_REF_SKU', 'QTY', 'NAME', 'ADDRESS', 'ADDRESS 2', 'ZIPCODE', 'CITY', 'COUNTRY', 'REFERENCE']
    print data
    NAME = data[4]
    if NAME in dictionary_data:
        dictionary_data[NAME]['Purchase_List']['QTY'].append(int(data[3]))
        dictionary_data[NAME]['Purchase_List']['Supplier_REF_SKU'].append(data[2])
    else:
        dictionary_data[NAME] =  {'Address':data[5], 'Address2':data[6], 'Zipcode':int(data[7]), 'City':data[8], 'Country':data[9], 'REFERENCE':data[10], 'Purchase_List':{'INVOICE_To':data[0], 'Customer_id':data[1], 'QTY':[int(data[3])],'Supplier_REF_SKU':[data[2]]}}
    
for i in dictionary_data:
    print i,":",dictionary_data[i],'\n'
    


#['STARCD173501', 'STARCF182801', '7PLUSF173202', '7PLUSF174501', 'MALTAE150301', 'ASTN180501']
