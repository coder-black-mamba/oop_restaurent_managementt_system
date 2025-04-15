from Restaurent import Restaurant
from User import Admin, Employee
from Menu import MenuItem , Menu
from Customer import Customer

# main restaurant class
hanif_er_kalavuna =  Restaurant("Hanif Er Kalavuna", "Best Food in Town", "Dhaka")
admin =  Admin("Sayed", "123456789", "XXXXXXXXXXXXXXX", "Dhaka","12345")
# setting the restaurent
admin.set_restaurant(hanif_er_kalavuna)
# setting the admin
hanif_er_kalavuna.set_admin(admin=admin)

# ================== Employee ==================

# adding the employee
jd = Employee("John Doe", "123456789", "john@example.com", "Dhaka", 30, "Manager", 50000)
js = Employee("Jane Smith", "987654321", "jane@example.com", "New York", 25, "Developer", 60000)
# admin.add_employee(jd)
# admin.add_employee(js)
# view employee list
# admin.view_employee_list()
#
# hanif_er_kalavuna.hr.view_employee_list()

# ================== Admin ==================
item1 = MenuItem("Burger", 10, 50)
item2 = MenuItem("Pizza", 12, 30)
item3 = MenuItem("Fries", 5, 20)
item4 = MenuItem("Coke", 2, 10)
admin.add_menu_item(item1)
admin.add_menu_item(item2)
admin.add_menu_item(item3)
admin.add_menu_item(item4)

# ================== Customer ==================
# customer = Customer("John Doe", "123456789", "john@example.com", "Dhaka")
# customer.lock_restaurant(hanif_er_kalavuna)
# customer.view_menu()
# customer.add_to_cart(item1, 2)
# customer.add_to_cart(item3, 2)
# customer.add_to_cart(item4, 2)
# customer.view_cart()
# customer.pay_bill()
# customer.view_menu()

# menu system
print("===========================================================")
print("Welcome to OOP Restaurant Management System")
print("===========================================================")

name = input("Hello Sir Please Input Your Name : ")

def customer_menu(name,is_admin=False):
    if not is_admin:
        phone = input("Please Input Your Phone Number : ")
        email = input("Please Input Your Email : ")
        address = input("Please Input Your Address : ")
    else:
        name="admin"
        phone="*********"
        email="*********"
        address = "*********"


    customer = Customer(name, phone, email, address)
    customer.lock_restaurant(hanif_er_kalavuna)
    while True:
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            customer.view_menu()
        elif choice == "2":
            item_id = input("Enter the item ID: ")
            quantity = int(input("Enter the quantity: "))
            item = hanif_er_kalavuna.menu.find_item(item_id)
            print(hanif_er_kalavuna.menu.menu_items)
            if item is None:
                print("Invalid item ID.")
                continue
            customer.add_to_cart(item, quantity)
        elif choice == "3":
            customer.view_cart()
        elif choice == "4":
            customer.pay_bill()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
        print("===========================================================")


if name =="Sayed":
    password = input("Please Input Admin Password : ")
    if password==admin.password:
        while True:
            print("1. Add Employee")
            print("2. View Employee List")
            print("3. Delete Employee")
            print("4. View Menu Items")
            print("5. Add Menu Item")
            print("6. Delete Menu Item")
            print("7. Customer Mode")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("Enter employee name: ")
                phone = input("Enter employee phone: ")
                email = input("Enter employee email: ")
                address = input("Enter employee address: ")
                age = input("Enter employee age: ")
                designation = input("Enter employee designation: ")
                salary = input("Enter employee salary: ")
                employee = Employee(name, phone, email, address, age, designation, salary)
                admin.add_employee(employee)
            elif choice == "2":
                admin.view_employee_list()
            elif choice == "3":
                emp_id = input("Enter employee ID: ")
                admin.delete_employee(emp_id)
            elif choice == "4":
                admin.view_menu_items()
            elif choice == "5":
                name = input("Enter menu item name: ")
                price = int(input("Enter menu item price: "))
                quantity = int(input("Enter menu item quantity: "))
                item = MenuItem(name, price, quantity)
                admin.add_menu_item(item)
            elif choice == "6":
                item_id = input("Enter menu item ID: ")
                admin.delete_menu_item(item_id)
            elif choice == "7":
                customer_menu(name,True)
            elif choice == "8":
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Wrong Password")
else:
    customer_menu(name=name,is_admin=False)





