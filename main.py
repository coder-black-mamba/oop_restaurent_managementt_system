from Restaurent import Restaurant
from User import Admin, Employee
from Menu import MenuItem , Menu
from Customer import Customer


# main restaurant class
hanif_er_kalavuna =  Restaurant("Hanif Er Kalavuna", "Best Food in Town", "Dhaka")
admin =  Admin("Sayed", "123456789", "XXXXXXXXXXXXXXX", "Dhaka")
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
customer.add_to_cart(item1, 2)
customer.add_to_cart(item3, 2)
customer.add_to_cart(item4, 2)
customer.view_cart()
customer.pay_bill()
customer.view_menu()





