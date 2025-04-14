from utilities import unique_id
# Menu Class
class Menu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item):
        self.menu_items.append(item)

    def delete_item(self, item_id):
        for item in self.menu_items:
            if str(item.id) == item_id:
                self.menu_items.remove(item)
                print("Item deleted successfully.")
                return True
        print("Item Not Found")
    def find_item(self, item_id):
        for item in self.menu_items:
            if str(item.id) == item_id:
                return item
        return None
    # def view_menu_items(self):
    #     for item in self.menu_items:
    #         print(item)
    def view_menu_items(self):
        print("===================== Menu Item's ======================")
        print( f"  ID   |  Item  |  Price ")
        print("-----------------------------------------------------------")


        for item in self.menu_items:
            # print(item)
            print(f"{item.id}\t {item.name}\t {item.price} ")
        print("===========================================================")

# Menu Item
class MenuItem:
    def __init__(self, name, price, quantity):
        self.id = unique_id()
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"Item ID: {self.id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

