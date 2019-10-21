import datetime
from TotalTax import *

class SaleProduct(TotalTax):
    
    sale_product_detail = dict()
    
    def sale_product(self,saleProductDate,saleQuantity,saleVendorName,saleBasicPrice,saleTotalPrice,Type):
        """
        @Func :- It will manage the Sale Product 
        @Param1 :- saleProductDate is the product sale date and it's type is string
        @Param2 :- saleQuantity is the total sale product quantity and it's type is integer
        @Param3 :- saleVendorName is the name of the vendor and it's type is string
        @Param4 :- saleBasicPrice is the sale Basic Price and it's type integer
        @Param5 :- saleTotalPrice is the Total sale Price and it's type is integer
        @Return :- It will return the total sale product detail
        """
        saleTotalTax = totaltax.getSaleTax(saleTotalPrice,Type)
        saleOrderNumber = 'SO/0000' + str(len(self.sale_product_detail)+1)
        self.sale_product_detail[len(self.sale_product_detail)+1] = {'ordernumber':saleOrderNumber,'date':saleProductDate,'qty':saleQuantity,'vendorname':saleVendorName,'basicprice':saleBasicPrice,'totalprice':saleTotalPrice,'totaltax':saleTotalTax}    

totaltax = TotalTax()
