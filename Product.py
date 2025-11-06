#Phase 1: Modelling a single product
class Product():
    def __init__(self, pID, name, price, quantity):
        self.pID = pID
        self.name = name
        self.price = price
        self.quantity = quantity


    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"
    
    def correct_Name(self):
        if not self.name.isalpha():
            raise ValueError("product is entered incorrectly")
        return True
    
    def correct_Price(self):
        if self.price < 0:
            raise ValueError("Product price mustn't be negative value")
        return True
    
    def updatePrice(self, quantity):
        newPrice= self.price * quantity
        return newPrice
    

#phase 3: handling special products
class electronics(Product):
    def __init__(self, pID, name, price, quantity, warranty):
        super().__init__(pID, name, price, quantity)
        self.warranty = warranty
    
    def trackWarranty(self, monthUsed):
        if monthUsed > self.warranty:
            return "Warranty expired"
        else:
            return "Warranty valid"
    
    def __str__(self):
        superStr = super().__str__()
        return f"{superStr}, warranty={self.warranty} months"
    
class clothing(Product):
    def __init__(self, pID, name, price, quantity, size, color):
        super().__init__(pID, name, price, quantity)
        self.size = size
        self.color = color
    
    def __str__(self):
        superStr = super().__str__()
        return f"{superStr}, size={self.size}, color={self.color}"
       






















