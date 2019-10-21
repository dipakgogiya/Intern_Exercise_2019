import xlrd

#file_location = "/home/emipro/Downloads/import_sale_order_Final.xlsx"

workbook_data = xlrd.open_workbook("import_sale_order_Final.xlsx")

sheet = workbook_data.sheet_by_index(0)

dictionary_data= dict()

"""
print sheet.cell_value(0,0)  ROW is 0 and Column is 0
print sheet.nrows  nrows is represent Total Number of Rows 
print sheet.ncols ncols is represent Total Number of Columns

for col in range(sheet.ncols): #It iterate length of all the columns
    print sheet.cell_value(0,col)  #Print All The Columns
"""

for rows in range(1,sheet.nrows):
    city = str(sheet.cell_value(rows,8).encode('ascii', 'ignore').decode('ascii'))   #It Convert the whole unicode string which is special character in string format
    if str(sheet.cell_value(rows,4)) in dictionary_data:
            dictionary_data[str(sheet.cell_value(rows,4))]['Purchase_List']['QTY'].append(int(sheet.cell_value(rows,3)))
            dictionary_data[str(sheet.cell_value(rows,4))]['Purchase_List']['Supplier_REF_SKU'].append(str(sheet.cell_value(rows,2)))        
    else:
            dictionary_data[str(sheet.cell_value(rows,4))] =  {'Address':str(sheet.cell_value(rows,5)), 'Address2':str(sheet.cell_value(rows,6)), 'Zipcode':int(sheet.cell_value(rows,7)), 'City':city, 'Country':str(sheet.cell_value(rows,9)), 'REFERENCE':str(sheet.cell_value(rows,10)), 'Purchase_List':{'INVOICE_To':str(sheet.cell_value(rows,0)), 'Customer_id':str(sheet.cell_value(rows,1)), 'QTY':[int(sheet.cell_value(rows,3))],'Supplier_REF_SKU':[str(sheet.cell_value(rows,2))]}}

        
for i in dictionary_data:
    print i ,":",dictionary_data[i],'\n'
