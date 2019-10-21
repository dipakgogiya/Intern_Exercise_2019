import xlrd

#file_location = "import_sale_order_Final.xlsx"

workbook_data = xlrd.open_workbook("import_sale_order_Final.xlsx")

sheet = workbook_data.sheet_by_index(0)



"""
print sheet.cell_value(0,0)  ROW is 0 and Column is 0
print sheet.nrows  nrows is represent Total Number of Rows 
print sheet.ncols ncols is represent Total Number of Columns

for col in range(sheet.ncols): #It iterate length of all the columns
    print sheet.cell_value(0,col)  #Print All The Columns
"""
first_list = []
second_list = []
for rows in range(1,sheet.nrows):
   	first_list.append(str(sheet.cell_value(rows,0)))
	second_list.append(str(sheet.cell_value(rows,1)))

print first_list
print second_list
	
