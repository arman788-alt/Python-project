# Question
# Python Week 2 Practice Day 02

#1. Write what is meant by operator overloading and method overriding with examples.

# class Person:
#     def __init__(self, name, age, height, weight) -> None:
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight

# class Cricketer(Person):
#     def __init__(self, name, age, height, weight) -> None:
#         super().__init__(name, age, height, weight)

# sakib = Cricketer('Sakib', 38, 68, 91)
# musfiq = Cricketer('Rahim', 36, 68, 88)
# kamal = Cricketer('Kamal', 39, 68, 94)
# jack = Cricketer('Jack', 38, 68, 91)
# kalam = Cricketer('Kalam', 37, 68, 95)

#2. Find out which of these players is older using the operator overloading.
#3. Write down 4 differences between the class method and static method with proper examples.
#4. Write what are getter and setter with proper examples
#5. Explain the difference between inheritance and composition with proper examples.





#1. Write what is meant by operator overloading and method overriding with examples.
# Method overriding: Method overriding occurs when a subclass provides a new 
# implementation for a method that is already defined in its superclass

class animal:
    def __init__(self,name):
        self.name = name


    def sound(self):
        print("Animal sound")


class dog(animal):
    def __init__(self,name):
        super().__init__(name)
    

    def sound(self):
        print("ghew ghew")


class cat(animal):
    def __init__(self,name):
        super().__init__(name)
    

    def sound(self):
        print("mew mewww")

kukur = dog("kukur")
# kukur.sound()

biral = cat("biral")
# biral.sound()

lst = [kukur, biral]

# for i in lst:
    # i.sound()




# Operator overloading:
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    

    def food(self):
        print("pizza,burger,cheicken")
    

    def exercise(self):
        print("khaidai ghumai")



class cricket(person):
    def __init__(self,name,age):
        super().__init__(name,age)

    

    def food(self):
        print("vegetables")
    

    def exercise(self):
        print("regular 30mins gym")
    

    def __repr__(self) -> str:

        self.food()
        self.exercise()
        return f"maintaim everyting"



shakib = cricket("shakib", 38)
# print(shakib)


    


#2. Find out which of these players is older using the operator overloading.


class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)


    

sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)




# sultion:04
# Class method vs Static Method
# The difference between the Class method and the static method is:

# A class method takes cls as the first parameter(self) while a static method needs no specific parameters.
# A class method can access or modify the class state while a static method can’t access or modify it.
# In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
# We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.



# solution-05
# Inheritance (IS-A relationship)
# Inheritance is when a class inherits attributes and behaviors (methods) from another class. It's like saying:

# “A Dog is a type of Animal.”

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

# Dog inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

# Usage
dog = Dog("Buddy")
# print(dog.speak())  # Output: Buddy barks





# Composition (HAS-A relationship)
# Composition means one class contains another class. It's like saying:

# “A Car has a Engine.”

# You're combining simple classes into more complex ones.

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS an Engine

    def start(self):
        return self.engine.start()

# Usage
my_car = Car()
# print(my_car.start())  # Output: Engine started



# Quick Comparison Table::
# Feature   	   Inheritance   	         Composition
# Relationship	      IS-A	                     HAS-A
# Code Reuse	  Inherited from base class	Uses. components inside
# Flexibility	    Less flexible	              More flexible
# Example	      Dog is an Animal	            Car has an Engine
