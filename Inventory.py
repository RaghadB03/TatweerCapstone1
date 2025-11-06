from Product import Product

#Building the inventory manager   

class Inventory():
    def __init__(self):
        self.products = {}
    
    def addProduct(self, product):
        if product.pID in self.products:
            raise ValueError("product already exist")
        self.products[product.pID] = product
   
    def updateStock(self, pID, quantity):
        if pID not in self.products:
            raise ValueError("product not exist")
        self.products[pID].quantity += quantity
   
    def lookupProduct(self, pID):
        if pID not in self.products:
            raise ValueError("Product doesn't exist")
        return self.products[pID]
    
    def lowStockAlert(self, alertQuntity):
        low_stock_products = []
        for product in self.products.values():
            if product.quantity < alertQuntity:
                low_stock_products.append(product)
        return low_stock_products