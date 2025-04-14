from User import User
from Cart import Cart


# The Customer Class
class Customer(User):
    def __init__(self, name, phone_number, email, address):
        super().__init__(name, phone_number, email, address)
        self.cart = Cart()
        self.restaurant=None
    def lock_restaurant(self, restaurant):
        self.restaurant = restaurant
        print(f"Hello! Mr/Mrs {self.name} :). Please Go With ..... {restaurant.name}.")

    def view_menu(self):
        self.restaurant.menu.view_menu_items()

    def add_to_cart(self, item, quantity):
        self.cart.add_item(item, quantity)

    def view_cart(self):
        self.cart.view_cart()

    def pay_bill(self):
        total = self.cart.calculate_total()
        print(f"====================== {self.restaurant.name} ======================")
        print(f"Total bill amount: {total}")
        self.cart.clear_cart()
        print("Bill paid successfully.")
        print(f"Thanks For Visiting {self.restaurant.name}. Come Again.")
        print(f"====================== Made With LV By Abu Sayed ======================")


