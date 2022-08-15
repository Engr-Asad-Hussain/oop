""" Introduction to Python overridding method """

# The overriding method allows a child class to provide a specific implementation of a method 
# that is already provided by one of its parent classes.
class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self._base_pay = base_pay

    @property
    def get_pay(self):
        return self._base_pay

emp = Employee('Asad Hussain', 20_000)
print(emp._base_pay)

class SalesEmployee(Employee):
    def __init__(self, name, base_pay, sales_incentive=None):
        self.name = name
        self._base_pay = base_pay
        self.sales_incentive = sales_incentive

    @property
    def get_pay(self):
        return super().get_pay + self.sales_incentive

sales = SalesEmployee('Asad Hussain', 30_000, 15_000)
print(sales.get_pay)

# The get_pay() property returns only the base_pay, not the sum of the base_pay and sales_incentive.

# When you call the get_pay() from the instance of the SalesEmployee class, 
# Python executes the get_pay() method of the Employee class, which returns the base_pay.

emp = Employee('Asad Hussain', 10_000)
print(emp.get_pay)
sales = SalesEmployee('Asad Hussain', 45_000, 5_000)
print(sales.get_pay)
# When you call the get_pay() method of the SalesEmployee‘s object, Python will call the 
# get_pay() method in the SalesEmployee class:
# If you create an instance of the Employee class, Python will call the get_pay() method of 
# the Employee class, not the get_pay() method of the SalesEmployee class. For example:

""" Advanced method overriding example """
