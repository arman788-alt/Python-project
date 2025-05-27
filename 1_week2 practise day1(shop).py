# Python Week 2 Practice Day 01

# 1. Create a Product class and a Shop class.
# 2. Inside the Shop class, create a method name add_product which adds products using the Product class to the Shop class.

# 3. Inside the Shop class, create a method name buy_product which is used to buy a product and check whether this product is available or not. If you successfully buy a product, then throw a Congress message.

# 4. What is Inheritance? Explain with examples
# 5. What are Encapsulation and Access Modifiers? Explain with examples



class shop:

    def __init__(self):
        self.products = []
        self.cart = []

    
    def add_product(self,name,price,quantity):

        p = product(name, price,quantity)
        self.products.append(p)
        print(f"{name} product is successfully added in shop")

        

    def buy_product(self, name, quantity=1):

        for p in self.products:

         if name == p.name:
            if p.quantity>=quantity:
             self.cart.append(p)
             p.quantity-=quantity
             print(f"You successfully bought '{name}',quantity: {quantity}, Congratualtions! Remaining quantity of this product: {p.quantity}")
             return
            
            else:
                print(f"Sorry not enough Quantity of {p.name} beacuse quanitiy of this product: {p.quantity}")
                return
         
        print(f"Sorry, '{name}' does not exist in this shop.")
    

    def remove_from_cart(self,name):

        for i in self.cart:
            if i.name == name:
                self.cart.remove(i)
                print(f"{i.name} remove from cart.")
                return
        
        print(f"'{name}' not found in cart.")


             
    def display_cart_item(self):
        
        if not self.cart:
            print("Your cart is empty.")
            return

        print("Your cart items are :")
        for i in self.cart:

            print(f"{i.name}: price: {i.price} quantity: {i.quantity}")
       
        
        print(f"All cart item are displayed.")

    
    # Total bill
    def checkout(self):
        if not self.cart:
            print("Cart is empty. Nothing to checkout.")
            return

        print("Checkout Summary:")
        total = 0
        for item in self.cart:
            print(f"{item.name} - {item.price} x {item.quantity}")
            total += item.price * item.quantity

        print(f"Total Bill: {total} tk")
        print("Thank you for your purchase!")

        self.cart.clear()  # Empty the cart after checkout




    def __repr__(self):

        if not self.products:
            return f"No products available in this shop."

        for i in self.products:
            print(i)
        return f"All shop products displayed."
            


class product:

    def __init__(self,name, price, quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity
    

    def __repr__(self):
        return f"{self.name}: {self.price} {self.quantity}"
    


shopno = shop()

while True:
    print("All option!!")
    print("1.Product Add")
    print("2.Product Buy")
    print("3.Product Remove From cart")
    print("4.Display cart item")
    print("5.Product details")
    print("6.Total Bill")
    print("7.Exit")

    ch = input("Enter Choice your option: ")

    if ch == "1":
        name = input("Enter product name: ")
        price = int(input("Enter product price: "))
        quan = int(input("Enter product Quantity: "))
        shopno.add_product(name, price,quan)
    


    elif ch == "2":
        name = input("Enter product name: ")
        quan = int(input("Enter product Quantity: "))
        shopno.buy_product(name, quan)
    
    elif ch == "3":
        name = input("Enter product name: ")
        shopno.remove_from_cart(name)
    
    elif ch == "4":
        shopno.display_cart_item()

    elif ch == "5":
        print(shopno)
   
    elif ch == "6":
        shopno.checkout()
    
    elif ch == "7":
        break

    else:
        print("Invalid Choice")
    





















    




