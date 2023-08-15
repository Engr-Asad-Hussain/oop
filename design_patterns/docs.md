## Design Patterns
Design patterns are used to represent the pattern used by developers to create software or web application. These patterns are selected based on the requirement analysis. The patterns describe the solution to the problem, when and where to apply the solution and the consequences of the implementation.

## Model View Controller Pattern
- ```Model```: It consists of pure application logic, which interacts with the database. It includes all the information to represent data to the end user.
- ```View```: View represents the HTML files, which interact with the end user. It represents the model’s data to user.
- ```Controller```: It acts as an intermediary between view and model. It listens to the events triggered by view and queries model for the same.
- Reference(s):
  - https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_quick_guide.html


## Singleton Pattern
- This pattern restricts the instantiation of a class to one object. It is a type of creational pattern and involves only one class to create methods and specified objects.
- It provides a global point of access to the instance created.
- The number of instances created are same and there is no difference in the objects listed in output.
- Reference(s):
  - https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_quick_guide.html
