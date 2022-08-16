""" Introduction to Python Abstract Classes """

# In object-oriented programming, an abstract class is a class that cannot be instantiated. 
# However, you can create classes that inherit from an abstract class.

# Typically, you use an abstract class to create a blueprint for other classes.
# Similarly, an abstract method is an method without an implementation. An abstract class may 
# or may not include abstract methods.
# Python doesn’t directly support abstract classes. But it does offer a module that allows you 
# to define abstract classes.
# To define an abstract class, you use the abc (abstract base class) module.

""" Python abstract class example """

# Suppose that you need to develop a payroll program for a company.
# The company has two groups of employees: 
# # # full-time employees.
# # # hourly employees. 
# The full-time employees get a fixed salary while the hourly employees get paid by hourly 
# wages for their services.

# The payroll program needs to print out a payroll that includes employee names and their 
# monthly salaries.

# To model the payroll program in an object-oriented way, you may come up with the following 
# classes: Employee, FulltimeEmployee, HourlyEmployee, and Payroll.

class Employee:
    def __init__(self, first_name, last_name, salary=None):
        self.first_name = first_name
        self.last_name = last_name
        self._salary = salary

    def get_salary(self):
        return self._salary

class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name, salary)

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, rate=5_000):
        super().__init__(first_name, last_name)
        self.worked_hour = worked_hours
        self.rate = rate
    
    def get_salary(self):
        return self.worked_hour * self.rate

emp = Employee('Asad', 'Hussain', 20_000)
print(emp.__dict__)
fulltime = FulltimeEmployee('Amna', 'Arshad', 35_000)
print(fulltime.__dict__)
hourly = HourlyEmployee('Aisha', 'Habib', 20)
print(hourly.__dict__)

print(emp.get_salary())
print(fulltime.get_salary())
print(hourly.get_salary())
