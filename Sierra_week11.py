#DSC510
#Week11: Object Oriented Programming
#Programming Assignment Week11
#Author: Joanna Sierra-Mendoza
#02/23/24

import locale

class CashRegister:
    def __init__(self): #(setter)
        self.total = 0.0
        self.items = 0

    def addItem(self, price):
        self.items += 1
        self.total += price

    def getTotal(self):
        return self.total

    def getCount(self):
        return self.items

    def clearCart(self):
        self.total = 0.0
        self.items = 0

def main():
    print("~~~~Welcome to my Cash Register Program~~~~")
    register = CashRegister()
    while True:
        price = input("Enter the price of an item to add or 'quit' to END. Enter 'clear' to clear cart: ")
        price = price.lower()
        if price == "quit":
            break
        elif price == "clear":
            register.clearCart()
            print("\n*Cart Cleared*")
        try:
            price = float(price)
            register.addItem(price)
        except ValueError:
            print("ERROR: Invalid Input")
    locale.setlocale(locale.LC_ALL,"us")
    print("\nTotal number of items in cart: %d" % register.getCount())
    print("Total Price = %s" % locale.currency(register.getTotal()))
    print("\nThank you for using my program!")

if __name__ == "__main__":
    main()