""" Introduction to the Python Multiple inheritance """
# When a class inherits from a single class, you have single inheritance. 
# Python allows a class to inherit from multiple classes. 
# If a class inherits from two or more classes, you’ll have multiple inheritance.

class Car:
    def go(self):
        print('Going ...')

class Flyable:
    def fly(self):
        print('Flying ...')

class FlyingCar(Car, Flyable):
    # Since the FlyingCar inherits from Car and Flyable classes, it reuses the methods from those classes. 
    # It means you can call the go() and fly() methods on an instance of the FlyingCar class like this
    pass

fc = FlyingCar()
fc.go()
fc.fly()

""" Method resolution order (MRO) """
# When the parent classes have methods with the same name and the child class calls the method, 
# Python uses the method resolution order (MRO) to search for the right method to call. 
# Consider the following example