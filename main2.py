"""
2.1 Customer Features:

View Menu: Customers can browse through the restaurant's menu to explore available food and beverage options.

Add Item to Cart: Customers can add desired items to their shopping cart for ordering.

View Cart: Customers can view the contents of their cart, including item names, quantities, and prices.

Pay Bill: Customers can pay their bill, completing the transaction and clearing the cart.

Account Creation: Customers have the option to create an account with their name, phone number, email, and address for personalized services.

2.2 Admin Features:

Add New Item: Admins can add new items to the restaurant's menu, specifying details such as name, price, and quantity.

Add Employee: Admins can add new employees to the system, including details like name, phone number, email, address, age, designation, and salary.

View Employee List: Admins can view a list of all employees along with their details.

View Items: Admins can view the restaurant's menu, displaying available items along with their prices and quantities.

Delete Item: Admins can remove items from the menu, providing flexibility in menu management.



"""
# Restaurant
# ---> Admin , Customer , Employee -> User(ABC)
# ---> Menu -> FoodItem
# ---> Cart -> FoodItem


# Restaurant Class
"""
    name,
    tagline,
    location,
    menu(class)------->add new item
                      |->delete item  
                      |->view mwnu item  
    =======method=====
    add_employee  
    view_employee_list
    delete_employee

"""
from utilities import unique_id
from abc import ABC, abstractmethod


# Menu Class
class Menu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item):
        self.menu_items.append(item)

    def delete_item(self, item_id):
        for item in self.menu_items:
            if item.id == item_id:
                self.menu_items.remove(item)
                print("Item deleted successfully.")
                return True
        print("Item Not Found")

    def view_menu_items(self):
        for item in self.menu_items:
            print(item)


# Menu Item
class MenuItem:
    def __init__(self, name, price, quantity):
        self.id = unique_id()
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Item ID: {self.id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"


# user class abc
class User(ABC):
    def __init__(self, name, phone_number, email, address):
        self.id = unique_id()
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address


class Employee(User):
    def __init__(self, name, phone_number, email, address, age, designation, salary):
        super().__init__(name, phone_number, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.id}, Name: {self.name}, Age: {self.age}, Designation: {self.designation}, Salary: {self.salary}"

    def show_employee(self):
        print(
            f"Employee ID: {self.id}, Name: {self.name}, Age: {self.age}, Designation: {self.designation}, Salary: {self.salary}")


class Admin(User):
    def __init__(self, name, phone_number, email, address):
        super().__init__(name, phone_number, email, address)
        self.restaurant = None

    def set_restaurant(self, restaurant):
        self.restaurant = restaurant
        print("Restaurant set successfully.")

    def add_employee(self, employee):
        self.restaurant.hr.employee_list.append(employee)

    def view_employee_list(self):
        for employee in self.restaurant.hr.employee_list:
            print(employee)

    # menu section
    def view_menu_items(self):
        self.restaurant.menu.view_menu_items()

    def add_menu_item(self, item):
        self.restaurant.menu.add_item(item)

    def delete_menu_item(self, item_id):
        self.restaurant.menu.delete_item(item_id)


# the cart class
class Cart:
    def __init__(self):
        self.items = []

    def view_cart(self):
        for item in self.items:
            print(f"Item: {item['item'].name}, Quantity: {item['quantity']}")

    def add_item(self, item, quantity):
        self.items.append({"item": item, "quantity": quantity})
        print("Items Added To Cart Successfully!!!")

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


class HR:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def delete_employee(self, employee_id):
        for employee in self.employee_list:
            if employee.id == employee_id:
                self.employee_list.remove(employee)
                print("Employee deleted successfully.")
        print("Employee not found.")

    def view_employee_list(self):
        for employee in self.employee_list:
            print(employee)


# The Customer Class
class Customer(User):
    def __init__(self, name, phone_number, email, address):
        super().__init__(name, phone_number, email, address)
        self.cart = Cart()
        self.restaurant = None

    def set_restaurant(self, restaurant):
        self.restaurant = restaurant
        print("Restaurant set successfully.")

    def view_menu(self):
        self.restaurant.menu.view_menu_items()

    def add_to_cart(self, menu, item_id, quantity):
        for item in menu.menu_items:
            if item.id == item_id:
                if item.quantity >= quantity:
                    self.cart.add_item(item, quantity)
                    item.quantity -= quantity
                    print("Item added to cart successfully.")
                else:
                    print("Not enough quantity available.")
                return
        print("Item not found in the menu.")

    def view_cart(self):
        self.cart.view_cart()

    def pay_bill(self):
        total = self.cart.calculate_total()
        print(f"Total bill amount: {total}")
        self.cart.clear_cart()
        print("Bill paid successfully. Cart cleared.")


class Restaurant:
    def __init__(self, name, tagline, location):
        self.name = name
        self.tagline = tagline
        self.location = location
        # Menu Implementation
        self.menu = Menu()
        self.__hr = HR()
        self.__admin = None

    # add a check if admin is operating or not
    def set_admin(self, admin):
        self.__admin = admin

    @property
    def hr(self):
        return self.__hr


# main restaurant class
hanif_er_kalavuna = Restaurant("Hanif Er Kalavuna", "Best Food in Town", "Dhaka")
admin = Admin("Sayed", "123456789", "XXXXXXXXXXXXXXX", "Dhaka")
# setting the restaurent
admin.set_restaurant(hanif_er_kalavuna)
# setting the admin
hanif_er_kalavuna.set_admin(admin=admin)

# ================== Employee ==================

# adding the employee
# jd = Employee("John Doe", "123456789", "john@example.com", "Dhaka", 30, "Manager", 50000)
# js = Employee("Jane Smith", "987654321", "jane@example.com", "New York", 25, "Developer", 60000)
# admin.add_employee(jd)
# admin.add_employee(js)
# # view employee list
# admin.view_employee_list()
#
# hanif_er_kalavuna.hr.view_employee_list()

# add menu items
item1 = MenuItem("Burger", 10, 50)
item2 = MenuItem("Pizza", 12, 30)
item3 = MenuItem("Fries", 5, 20)
item4 = MenuItem("Coke", 2, 10)
admin.add_menu_item(item1)
admin.add_menu_item(item2)
admin.add_menu_item(item3)
admin.add_menu_item(item4)
# # view menu items
# admin.view_menu_items()
# # delete menu items
# # admin.delete_menu_item(item1.id)
# # admin.delete_menu_item(".iitem1d")
# admin.view_menu_items()
# ================== Customer ==================
customer = Customer("John Doe", "123456789", "john@example.com", "Dhaka")
customer.set_restaurant(hanif_er_kalavuna)
customer.view_menu()
customer.add_to_cart(hanif_er_kalavuna.menu, item1.id, 2)
customer.add_to_cart(hanif_er_kalavuna.menu, item2.id, 1)
customer.view_cart()
customer.pay_bill()
customer.view_menu()





