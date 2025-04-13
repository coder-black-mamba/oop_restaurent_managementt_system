from abc import ABC, abstractmethod
from utilities import  unique_id


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
        print(f"Employee ID: {self.id}, Name: {self.name}, Age: {self.age}, Designation: {self.designation}, Salary: {self.salary}")



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




