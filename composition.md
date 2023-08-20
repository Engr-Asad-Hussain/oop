## Composition: Favour composition over inheritance

Many of the design patterns in the ```Gang of Four Design Patterns``` book are based on the principle favour composition over inheritance. But what does that mean? Let's find out. If you want to separate responsibilities, create code with higher cohession, there's a couple of ways to do it. 
  1. One way to do it is inheritance. So instead of putting everything in one single big class, you would create a class hierarchy of classes and subclasses, where you would put certain things in a subclass so that it would be separated from the main class. 
  2. Another way you can do is composition. That means that you are basically using separate classes to represent separate things in the application. And then each of these classes use each other in some meaningful way. 

Its basically the difference between the ```is-a relationship``` which is inheritance and ```has-a relationship``` which is composition; allow you to separate responsibilities.
`#FFF asdasd`
The background color is `#ffffff` for light mode and `#000000` for dark mode.