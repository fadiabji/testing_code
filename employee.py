class Employee:
    """Class represent a employee"""
    def __init__ (self, first_name, last_name, salary):
        """initait one employee object"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, annual_raise=''):
        """Give the employee raise for anuual salary 5000 by defult otherwise enter the belop"""
        if annual_raise:
            self.salary = self.salary + int(annual_raise)
        else:
            self.salary += 5000
       
# my_employee = Employee('fadi','abji',30000)
# my_employee.give_raise()
# print(my_employee.salary)



