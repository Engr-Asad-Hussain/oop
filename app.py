""" Defining Attributes """
class Person:
    pass

person = Person()
# classes are callable
# 'Person' is the name of a class
# 'person' is the instance of Person

""" Defining Attributes """

# Python is dynamic it means we can define class attributes dynamically at runtime.
person.name = 'Asad Hussain'
person.age  = 20

print(person.name, person.age, Person())

# To define and initialize an attribute for all instances of a class, you use the __init__ method. 
# The following defines the Person class with two instance attributes name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# When you create a Person object, Python automatically calls the __init__ method to 
# initialize the instance attributes. 
# In the __init__ method, the self is the instance of the Person class.
person = Person('Asad Hussain', 20)
print(person.name, person.age)

""" Defining Instance Methods """

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = 20

    def greet(self):
        return f'Hey, Mr. {self.name}. Your age is found to be {self.age}'

person = Person('Asad Hussain', 20)
print(person.greet())

""" Define class attributes """

# Unlike instance attributes, class attributes are shared by all instances of the class.
# The following defines the counter class attribute in the Person class:
class Person:
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = 20

    def greet(self):
        return f'Hey, Mr. {self.name}'

print(Person.counter)

# You can also access class attributes from the instance of a class too.
person = Person('Asad Hussain', 20)
print(person.counter)

# To make the counter variable more useful, you can increase its value by one once an 
# object is created. 
# To do it, you increase the counter class attribute in the __init__ method:
class Person:
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

# The following creates two instances of the Person class and shows the value of the counter:
person1 = Person('Asad Hussain', 20)
person2 = Person('Aisha', 20)
print('counter', Person.counter)

""" Define class method """

# Like a class attribute, a class method is shared by all instances of the class. 
# The first argument of a class method is the class itself. 
# By convention, its name is cls. 
# Python automatically passes this argument to the class method. 
# Also, you use the @classmethod decorator to decorate a class method.
class Person:
    print('start class')
    counter = 0
    def __init__(self, name, age):
        print('1')
        self.name = name
        self.age = age
        print('2')

    @classmethod
    def create_anonymous(cls):
        print('3')
        return Person('Anonymous', 22)

print('4')
anonymous = Person.create_anonymous()
print('5')
print(anonymous)
print('6')
print(anonymous.name)