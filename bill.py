class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def calculate_gst(self):
        return 0.15 * self.calculate_total()  # Calculate 15% GST

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.calculate_total()
        return total

def generate_bill(cart):
    print("************ Shopping Complex ************")
    print("Item Name\tPrice\tQuantity\tTotal\tGST\tTotal with GST")
    print("----------------------------------------")
    
    for item in cart.items:
        total = item.calculate_total()
        gst = item.calculate_gst()
        total_with_gst = total + gst
        print(f"{item.name}\t\t{item.price}\t{item.quantity}\t\t{total:.2f}\t{gst:.2f}\t{total_with_gst:.2f}")

    print("----------------------------------------")
    print(f"Total Bill: {cart.calculate_total()}")

def main():
    cart = ShoppingCart()
    
    while True:
        name = input("Enter the item name (or 'q' to quit): ")
        if name == 'q':
            break
        
        price = float(input("Enter the item price: "))
        quantity = int(input("Enter the quantity: "))
        
        item = Item(name, price, quantity)
        cart.add_item(item)
    
    generate_bill(cart)

if __name__ == "__main__":
    main()
