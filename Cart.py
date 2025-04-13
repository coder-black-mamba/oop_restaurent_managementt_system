
# the cart class
class Cart:
    def __init__(self):
        self.items = []
    def view_cart(self):
        print("===================== Cart Item's ======================")
        print( f"Item | Quantity | Unit Price | Net Price |")
        print("-----------------------------------------------------------")


        for item in self.items:
            print(f"{item['item'].name}\t {item['quantity']} \t {item['item'].price}   {item['item'].price * (item['quantity'])}")
        print("-----------------------------------------------------------")
        print(f"Total: {self.calculate_total()}")
        print("===========================================================")

    def add_item(self, item, quantity):
    #     check quantity before updating
        if item.quantity >= quantity:
            self.items.append({"item": item, "quantity": quantity})
            item.quantity -= quantity
            print("Items Added To Cart Successfully!!!")
        else:
            print("Not enough quantity available.")

    def delete_item(self, item_id):
        for item in self.items:
            if item['item'].id == item_id:
                self.items.remove(item)
                print("Item deleted successfully.")
        print("Item not found.")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['item'].price * item['quantity']
        return total

    def clear_cart(self):
        self.items = []

