""" Introduction to the Python Enumeration """

# By definition, an enumeration is a set of members that have associated unique constant values. 
# Enumeration is often called enum.

from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    
# Note that the enumeration’s members are constants. Therefore, their names are in uppercase letters 
# by convention.
# In this example, the Color is an enumeration. The RED, GREEN, and BLUE are members of the Color 
# enumeration. They have associated values 1, 2, and 3.

print(type(Color))      # <class 'enum.EnumMeta'>
print(type(Color.RED))  # <enum 'Color'>
print(isinstance(Color.RED, Color)) # True
print(isinstance(Color.RED, Enum))  # True

# And it has the name and value attributes:
print(Color.RED.name, type(Color.RED.name))
print(Color.RED.value)

""" Membership and equality """
# To check if a member is in an enumeration, you use the in operator
if Color.RED in Color:
    print('RED is the member of Enum Color')
    
""" Access an enumeration member by name and value """
print(Color.RED, type(Color.RED))
print(Color['RED'], type(Color['RED']))

# Since an enumeration is callable, you can get a member by its value. 
# For example, the following return the RED member of the Color enumeration by its value:
print(Color(1))
print(Color(2))