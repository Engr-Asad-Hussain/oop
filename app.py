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