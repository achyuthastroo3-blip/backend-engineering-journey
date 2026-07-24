Today I cover the advanced topics in OOP 
Encapsulation
Polymorphism
Abstraction
super()
Method Overriding
Runtime Polymorphism
IS-A vs HAS-A
Composition vs Inheritance

Encapsulation:
It is used to protect the sensitive data, so that if we secure our data with using (__Value), now it is fully encapusaled 

Polymorphism:
it is a process to pass the empty varaibles to child classes by using pass

Abstraction
BY using abstraction we just showing the what the user want reaming process are storeing the back side the best example is user comes to atm with two diffrent bank accounts

super():
by using the super we are accessing the parent class methods by using super() in child class

Method Overriding:
It is used to access the class with another class but it has one role that is the starting class (parent class) is called by child class but there is no chance to call the child class by parent class

Runtime Polymorphism:
If we have no.of classes we combine them into one list by using "[]" and calling them "for value in values:" it automatically detect the method 

IS-A vs HAS-A:

IS-A
Dog IS-A Animal
Developer IS-A Employee

HAS-A
Car HAS-A Engine
Workflow HAS-A Trigger
Company HAS Employees



DSA PROBLEMS:

problem-01:
question : Chef lives at position x on the x - axis.
Chef has 2y friends, each living at every integer point in the range: [x − y, x + y] except the position x itself.
Chef wants to visit his friends, but his mother has placed a strict rule: Chef is allowed to travel at most z units away from his home in either direction. This means Chef can only move within the interval [x − z, x + z].
Your task is to determine how many of Chef’s friends live within the range Chef is allowed to travel.

approach:
there is a one clue that is 2y because - values ans postive so i just find min value of y and z and then multiply with 2

problem-02:
question : Write a program to check whether a triangle is valid or not, when the three angles of the triangle are the inputs. A triangle is valid if the sum of all the three angles is equal to 180 degrees.

approach:
i create a variable sum in that there is sum of a and b and c if the sum is equal to 180 its print yes else no 