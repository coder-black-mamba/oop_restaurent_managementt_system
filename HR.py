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
