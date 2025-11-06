from Product import Product, electronics, clothing
from Inventory import Inventory 

#phase 4: creating the manager's interface
def main():
    inventory = Inventory()
    
    # Adding products
    p1 = electronics(pID=1, name="Laptop", price=1000, quantity=10, warranty=24)
    p2 = clothing(pID=2, name="t-Shirt", price=20, quantity=50, size="m", color="Red")
    
    inventory.addProduct(p1)
    inventory.addProduct(p2)

     # Looking up products
    product = inventory.lookupProduct(pID=1)
    print(product)
    print(product.trackWarranty(monthUsed=12))
    
    product2 = inventory.lookupProduct(pID=2)
    print(product2)
   
    
    #update stock for a product
    inventory.updateStock(pID=2, quantity=-10)
    print(inventory.lookupProduct(pID=2))

    #see a list of all products currently in inventory
    lst=[]
    for pID, product in inventory.products.items():
        lst.append(product)
        print(product)
 
    

if __name__ == "__main__":
    main()
