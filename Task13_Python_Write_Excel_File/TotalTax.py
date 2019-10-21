class TotalTax(object):
    def getPurchaseTax(self,purchaseProductTotalPrice):    
        """
        @Func :- It will calculate the tax for purchase_product() method.
        @Param1 :- purchaseProductTotalPrice is the total Price of the purchase products and it's type is integer
        @Return :- It will return the total purchaseProductPrice with tax calculate
        """ 
        purchaseProductTotalPrice += (purchaseProductTotalPrice * 0.10) + (purchaseProductTotalPrice * 0.12)
        return purchaseProductTotalPrice
        
    def getSaleTax(self,saleTotalPrice,Type):
        """
        @Func :- It will calculate the tax for sale_product() method.
        @Param1 :- saleTotalPrice is the total Price of the sale products and it's type is integer
        @Param1 :- Type is the product Type and it's type is string
        @Return :- It will return the total saleProductPrice with tax calculate
        """ 
        if Type == "consumable" or Type == "stock":
            saleTotalPrice += (saleTotalPrice * 0.10) + (saleTotalPrice * 0.12)
            return saleTotalPrice
        else:
            saleTotalPrice += (saleTotalPrice * 0.18) + (saleTotalPrice * 0.12)
            return saleTotalPrice
