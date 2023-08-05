<!DOCTYPE html>
<html><head><style>
.red {
    color: red;
}
.blue {
    color: blue;
}
</style></head><body>

## Python Object-Oriented Programming
This Python OOP explains to you the Python object-oriented programming clearly so that you can apply it to develop software more effectively.

By the end of this Python OOP module, you’ll have good knowledge of object-oriented principles. And you’ll know how to use Python syntax to create reliable and robust software applications.

## Content
- Section 1. Classes and objects
  - [Introduction to Python Object-oriented programming]()


## Objects
- An object is a container that contains <span class="red">data</span> and <span class="red">functionality</span>.
- The <span class="red">data</span> represents the object at a particular moment in time. Therefore, the data of an object is called the <span class="red">state</span>. Python uses <span class="red">attributes<span> to model the state of an object.
- The <span class="red">functionality</span> represents the behaviors of an object. Python uses functions to model the behaviors. When a function is associated with an object, it becomes a <span class="red">method</span> of the object.
- In other words, an object is a container that contains the <span class="red">state</span> and <span class="red">methods</span>.
- Before creating objects, you define a class first. And from the class, you can create one or more objects. The objects of a class are also called <span class="red">instances</span> of a class.
- Everything in Python is an object, including classes.

## Class
- To define a <span class="red">class</span> in Python, you use the class keyword followed by the class name and a colon.
- By convention, you use capitalized names for classes in Python. If the class name contains multiple words, you use the <span class="red">CamelCase</span> format, for example <span class="red">SalesEmployee</span>.

When printing out the person object, you’ll see its name and memory address:
```py
<__main__.Person object at 0x000001C46D1C47F0>
```

## Class Variables
- Class variables are bound to the class. They’re shared by all instances of that class.

The following example adds the <span class="red">extension</span> and <span class="red">version</span> class variables to the <span class="red">HtmlDocument</span> class:
```py
class HtmlDocument:
    extension = 'html'
    version = 5
```
Both extension and version are the class variables of the HtmlDocument class. They’re bound to the HtmlDocument class.

### Get the values of class variables
To get the values of class variables, you use the dot notation <span class="red">(.)</span>. For example:
```py
HtmlDocument.extension # html
HtmlDocument.version # 5
```
If you access a class variable that doesn’t exist, you’ll get an <span class="red">AttributeError</span> exception. For example:
```py
HtmlDocument.media_type # AttributeError: type object 'HtmlDocument' has no attribute 'media_type'
```
Another way to get the value of a class variable is to use the <span class="red">getattr()</span> function. The getattr() function accepts an object and a variable name. It returns the value of the class variable. For example:
```py
extension = getattr(HtmlDocument, 'extension') # html
```
If the class variable doesn’t exist, you’ll also get an AttributeError exception. To avoid the exception, you can specify a <span class="red">default value</span> if the class variable doesn’t exist like this:
```py
media = getattr(HtmlDocument, 'media', 'text/html') # text/html
```

### Set values for class variables
To set a value for a class variable, you use the <span class="red">dot</span> notation:
```py
HtmlDocument.version = 10
```
or you can use the <span class="red">setattr()</span> built-in function:
```py
setattr(HtmlDocument, 'version', 10)
```
Since Python is a <span class="red">dynamic language</span>, you can add a class variable to a class at <span class="red">runtime</span> after you have created it. For example, the following adds the <span class="red">media_type</span> class variable to the <span class="red">HtmlDocument</span> class:
```py
HtmlDocument.media_type = 'text/html'
print(HtmlDocument.media_type)
```
Similarly, you can use the <span class="red">setattr()</span> function:
```py
setattr(HtmlDocument, media_type, 'text/html')
print(HtmlDocument.media_type)
```

### Delete class variables
To delete a class variable at runtime, you use the <span class="red">delattr()</span> function:
```py
delattr(HtmlDocument, 'version')
```
Or you can use the <span class="red">del</span> keyword:
```py
del HtmlDocument.version
```

## Class variable storage
Python stores class variables in the ```__dict__``` attribute. The __dict__ is a mapping proxy, which is a dictionary. For example:
```py
from pprint import pprint

class HtmlDocument:
    extension = 'html'
    version = '5'

HtmlDocument.media_type = 'text/html'
pprint(HtmlDocument.__dict__)

mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument' objects>,
              '__doc__': None,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'HtmlDocument' objects>,
              'extension': 'html',
              'media_type': 'text/html',
              'version': '5'})
```
As clearly shown in the output, the ```__dict__``` has three class variables: extension, media_type, and version besides other predefined class variables.

Python does not allow you to change the __dict__ directly. For example, the following will result in an error:
```py
HtmlDocument.__dict__['released'] = 2008
# TypeError: 'mappingproxy' object does not support item assignment
```
However, you can use the <span class="red">setattr()</span> function or dot notation to indirectly change the __dict__ attribute.

Also, the key of the __dict__ are strings that will help Python speeds up the variable lookup.

Although Python allows you to access class variables through the __dict__ dictionary, it’s not a good practice. Also, it won’t work in some situations. For example:
```py
print(HtmlDocument.__dict__['type']) # BAD CODE
```
When you add a function to a class, the function becomes a class attribute. Since a function is callable, the class attribute is called a callable class attribute.

## Instance Method
- By definition, a <span class="red">method</span> is a function that is bound to an <span class="red">instance</span> of a class.
- When you define a function inside a class, it’s purely a function. However, when you call the function via an instance of a class, the function becomes a method. Therefore, a method is a function that is bound to an instance of a class.
- A method has the first argument <span class="red">(self)</span> as the object to which it is bound.
- Python automatically passes the bound object to the method as the first argument. By convention, its name is self.

## Instance Variables
- In Python, <span class="red">class variables</span> are bound to a <span class="red">class</span> while <span class="red">instance variables</span> are bound to a <span class="red">specific instance of a class</span>. The instance variables are also called <span class="red">instance attributes.
- Python stores instance variables in the ```__dict__``` attribute of the instance. Each instance has its own ```__dict__``` attribute and the keys in this __dict__ may be different.
- When you access a variable via the instance, Python finds the variable in the __dict__ attribute of the instance. If it cannot find the variable, it goes up and look it up in the __dict__ attribute of the class.

The following defines a <span class="red">HtmlDocument</span> class with two class variables:

```py
from pprint import pprint

class HtmlDocument:
    version = 5
    extension = 'html'

pprint(HtmlDocument.__dict__)
print(HtmlDocument.extension) # html
print(HtmlDocument.version) # 5

mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument' objects>,
              '__doc__': None,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'HtmlDocument' objects>,
              'extension': 'html',
              'version': 5})
```
The HtmlDocument class has two class variables: <span class="red">extension</span> and <span class="red">version</span>. Python stores these two variables in the ```__dict__``` attribute.

When you access the class variables via the class, Python looks them up in the __dict__ of the class. The following creates a new instance of the <span class="red">HtmlDocument</span> class:
```py
home = HtmlDocument()
```
The <span class="red">home</span> is an <span class="red">instance</span> of the HtmlDocument class. It has its own ```__dict__``` attribute:

```py
pprint(home.__dict__) # {}
```
The ```home.__dict__``` is now empty. The home.__dict__ stores the instance variables of the home object like the ```HtmlDocument.__dict__``` stores the class variables of the HtmlDocument class.

Since a <span class="red">dictionary</span> is <span class="red">mutable</span>, you can mutate it e.g., adding a new element to the dictionary. Python allows you to access the class variables from an instance of a class. For example:
```py
print(home.extension)
print(home.version)
```
In this case, Python looks up the variables <span class="red">extension</span> and <span class="red">version</span> in ```home.__dict__``` first. If it doesn’t find them there, it’ll go up to the class and look up in the ```HtmlDocument.__dict__```

However, if Python can find the variables in the __dict__ of the instance, it won’t look further in the __dict__ of the class.

The following defines the <span class="red">version</span> variable in the home object:
```py
home.version = 6
print(home.__dict__)
```
Python adds the version variable to the ```__dict__``` attribute of the home object:
The __dict__ now contains one instance variable:

```py
{'version': 6}
```
If you access the version attribute of the home object, Python will return the value of the version in the ```home.__dict__``` dictionary:
```
print(home.version) # 6
```
If you change the class variables, these changes also reflect in the instances of the class:
```
HtmlDocument.media_type = 'text/html'
print(home.media_type) # text/html
```

## Class Methods
- <span class="red">Instance methods</span> are bound to a <span class="red">specific instance of a class</span>.
- Instance methods can access instance attributes within the same class. To invoke instance methods, you need to create the instance of a class first.
- To create the <span class="red">class method</span>, you place <span class="red">@classmethod</span> decorator above the method definition. Rename the <span class="red">self</span> parameter to <span class="red">cls</span> as a first parameter.
- Class methods can't access instance attributes. It can only access class attributes.
- To call the class methods you use classname followed by dot and then the method name ```ClassName.MethodName()```.
- When to use class methods?: You can use class methods for any methods that are not bound to a specific instance but the class. In practice, you often use class methods for methods that create an <span class="red">instance of the class</span>. When a method creates an instance of the class and returns it, the method is called a <span class="red">factory method</span>.
- Following is the difference between class methods and instance methods:
  S.No | Features | class methods | Instance methods
  -------- | -------- | -------- | --------
  1 | Binding |	Class	| An instance of the class 
  2 | Calling	| Class.method() | object.method()
  3 | Accessing	| Class attributes | Instance & class attributes
- Reference: https://www.pythontutorial.net/python-oop/python-class-methods/

## Encapsulation & Private Attributes
- <span class="red">Encapsulation</span> is one of the four fundamental concepts in object-oriented programming including <span class="red">abstraction</span>, <span class="red">encapsulation</span>, <span class="red">inheritance</span>, and <span class="red">polymorphism</span>.
- Encapsulation is the packing of data and functions that work on that data within a single object. By doing so, you can hide the internal state of the object from the outside. This is known as <span class="red">information hiding</span>.
- Encapsulation is the packing of data and methods into a class so that you can hide the information and <span class="red">restrict access</span> from outside.
- The idea of information hiding is that if you have an attribute that isn’t visible to the outside, you can control the access to its value to make sure your object is always has a <span class="red">valid state</span>.
- <span class="red">Private attributes</span> can be only accessible from the methods of the class. In other words, they cannot be accessible from outside of the class. Python doesn’t have a concept of private attributes. In other words, all attributes are accessible from the outside of a class. By convention, you can define a private attribute by prefixing a single underscore <span class="red">(_)</span> ```_attribute```.
- If you prefix an attribute name with double underscores <span class="red">(__)</span> like this: ```__attribute``` Python will automatically change the name of the __attribute to: ```_class__attribute```. This is called the <span class="red">name mangling</span> in Python. By doing this, you cannot access the ```__attribute``` directly from the outside of a class like: ```instance.__attribute```. However, you still can access it using the _class__attribute name: ```instance._class__attribute```
- Reference: https://www.pythontutorial.net/python-oop/python-private-attributes/


## Class Attributes
- A class attribute is shared by all instances of the class. To define a class attribute, you place it outside of the ```__init__()``` method.
- Use ```class_name.class_attribute``` or ```object_name.class_attribute``` to access the value of the class_attribute.
- When you access an attribute via an <span class="red">instance</span> of the class ```circle.pi``` Python searches for the attribute in the instance attribute list. If the instance attribute list doesn’t have that attribute, Python continues looking up the attribute in the <span class="red">class attribute</span> list. Python returns the value of the attribute as long as it finds the attribute in the instance attribute list or class attribute list. However, if you access an attribute directly ```Circle.pi```, Python directly searches for the attribute in the class attribute list.
- Use class attributes for <span class="red">storing class contants</span>, <span class="red">track data across all instances</span>, and <span class="red">setting default values for all instances of the class</span>.
  1. Since a constant doesn’t change from instance to instance of a class, it’s handy to store it as a class attribute.
  2. Tracking data across of all instances: When a new instance gets created, the constructor adds the instance to the list.
  3. Sometimes, you want to set a default value for all instances of a class. In this case, you can use a class attribute.
- Reference: https://www.pythontutorial.net/python-oop/python-class-attributes/


## Static Methods
- <span class="red">Static methods</span> aren’t bound to an <span class="red">object</span>. In other words, static methods cannot access and modify an object state.
- In addition, Python doesn’t implicitly pass the <span class="red">cls</span> parameter (or the <span class="red">self</span> parameter) to static methods. Therefore, static methods cannot access and modify the <span class="red">class’s state</span>.
- Use static methods to define <span class="red">utility</span> methods or group a logically related functions into a class.
- Use the <span class="red">@staticmethod</span> decorator to define a static method.
- Following is the difference between class methods and static methods:
  S.No | Class Methods	| Static Methods
  -------- | -------- | --------
  1 | Python implicitly pass the cls argument to class methods.	| Python doesn’t implicitly pass the cls argument to static methods
  2 | Class methods can access and modify the class state.	| Static methods cannot access or modify the class state.
  3 | Use @classmethod decorators to define class methods.	| Use @staticmethod decorators to define static methods.

## Property
- Use the Python <span class="red">property()</span> class to define a property for a class.
- Lets have a class with two attributes <span class="red">name</span> and <span class="red">age</span>. Since age is an instance of a class, you can assign it a new value using ```person.age = 12```. The following assignment is also technically valid ```person.age = -2``` but not logically. So, every time you need to check using <span class="red">if/else</span> condition ```person.age > 0```. To avoid the repetitive code you will use <span class="red">getter</span> and <span class="red">setter</span> methods in the ```Person``` class. But this strategy will not work with backward compatibility.
- By convention the getter and setter have the following name: ```get_<attribute>()``` and ```set_<attribute>()```.
- User property on the class variables for backward compatibility also. 
- ```property(fget=None, fset=None, fdel=None, doc=None)```
- Reference: 
  - https://www.pythontutorial.net/python-oop/python-properties/
  - https://realpython.com/python-property/


## Property Decorator
- You can user property on the class variables. To get the age of a Person object, you can use either the <span class="red">age</span> property or the <span class="red">get_age()</span> method. This creates an <span class="red">unnecessary redundancy</span>.
- To avoid redundancy you use <span class="red">@property</span> on getter (props) and <span class="red">@props.setter</span> on the setter.
- Use the <span class="red">@property</span> decorator to create a property for a class.
- You can create read-only property by creating only the getter property on the attribute.
- Reference: 
  - https://www.pythontutorial.net/python-oop/python-property-decorator/
  - https://realpython.com/python-property/