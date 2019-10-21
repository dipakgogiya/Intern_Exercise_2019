from TotalTax import *
import datetime

class PurchaseProduct(TotalTax):

    purchase_product_detail = dict()
    def purchase_product(self,purchaseProductDate,purchaseProductQuantity,purchaseProductVendorName,purchseProductBasicPrice,purchaseProductTotalPrice):
        """
        @Func :- It will manage the Purchase Product 
        @Param1 :- purchaseProductDate is the product purchase date and it's type is string
        @Param2 :- purchaseProductQuantity is the total purchase product quantity and it's type is integer
        @Param3 :- purchaseProductVendorName is the name of the customer and it's type is string
        @Param4 :- purchseProductBasicPrice is the Basic Price and it's type integer
        @Param5 :- purchaseProductTotalPrice is the Total Product Price and it's type is integer
        @Return :- It will return the total purchase product detail 
        """
        purhaseProductTotalTax = total.getPurchaseTax(purchaseProductTotalPrice)
        purchaseOrderNumber = 'PO/0000' + str(len(self.purchase_product_detail)+1)
        self.purchase_product_detail[len(self.purchase_product_detail)+1] = {'ordernumber':purchaseOrderNumber,'date':purchaseProductDate,'qty':purchaseProductQuantity,'vendorname':purchaseProductVendorName,'basicprice':purchseProductBasicPrice,'totalprice':purchaseProductTotalPrice,'totaltax':purhaseProductTotalTax}  

total = TotalTax()
