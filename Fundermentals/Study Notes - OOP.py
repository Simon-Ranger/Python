"""
This file contains in the following order:
1. Classes & Objects (OOP):
        Creating a Class and Object
    Parameter
    MetaClass
2. Magic Methods:
    __init__
    __str__
3. Iterators:
    Iterator vs Iterable
    Creating
    Stopping
4. Inheritance:
    Parent and Child Class
5. Objects:
    Modify and Delete Properties
6. Adding Functions:
    Super
7. Properties & Objects
8. Exercise
"""

#######################################################################################################################
#                                            CLASSES AND OBJECTS (OOP)                                                #
#######################################################################################################################
"""
Object-Oriented Programming (OOP) is the best and cleanest way to write code as it keeps things very organised,
since pretty much everything in python is an object with properties and methods. The class acts as a constructor or
simply a blueprint for everything.
"""

################################################## Creating a Class and Object ########################################
print(f"\n{'Creating a Class and Object':#^65}")
"""Simple forms that don't really do much in actual code"""


class MyClass:  # creates the class
    a = 1


b1 = MyClass()  # creates the object
print(f"These forms don't really do much but are critical for basic fundamental learning! ----> {b1.a}")

#######################################################################################################################
#                                                   Parameter                                                         #
#######################################################################################################################
print(f"\n{'Adding Parameters':#^65}")
"""
The parameter for a class is self which references the current instance of the class, used to access variables
belonging to it. You can rename it whatever you like as long as it's the first parameter of any function.
"""


class Person:
    def __init__(random, name, age):
        random.name = name
        random.age = age

    def myfunc(hello):
        print(f"Hello, my self is ----> {hello.name} <---- and I'm ----> {hello.age} <---- years old")


p1 = Person("Simon", 32)
p1.myfunc()

#######################################################################################################################
#                                                METACLASS                                                            #
#######################################################################################################################
print(f"\n{'Exploring Meta Classes':#^65}")
"""
These are similarly structured to a class but inherit from the type and is called automatically when the class having a
metaclass in it ends, if a metaclass keyword is used it will be called instead of the type. A Singleton is a pattern 
designed to restrict the instantiation of a class to a single object, it's used in situations where exactly 1 
object is required.
"""


class Study(type):
    def __new__(mcs, name, bases, class_dict):
        class_ = super().__new__(mcs, name, bases, class_dict)
        class_.freedom = True
        return class_


class Book(object, metaclass=Study):
    def __init__(self, name):
        self.name = name


print(f"{Book.__dict__}")

#######################################################################################################################
#                                                MAGIC METHODS                                                        #
#######################################################################################################################

################################################### __init__ ##########################################################
print(f"\n{'Revisiting the __init__ Function':#^65}")
"""
Every class has the build-in function __init__ which executes when a class is being started, you use this function
to assign values to properties or operations needed to do when creating the object.
"""


class Student:
    def __init__(self, name, age):  # takes the parameters "self" and "age"
        self.name = name  # makes it so "self" is part of the object
        self.age = age


S1 = Student("Simon", 32)
print(f"I am using the '__init__ function to use the previous data making my self still be {S1.name} "
      f"and my age is still ----> {S1.age} ")

#################################################### __str__ ##########################################################
print(f"\n{'The __str__ Function':#^65}")
"""This controls what should be returned when the object is represented as a string, it's not set"""


class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # represents the class as a string
        return f"{self.name}({self.age})"  # class the properties


S2 = Teacher("Simon", 32)
print(f"Controlling things is always fun, so lets control what is returned! by representing the string. We can "
      f"do this by adding () around our age! ----> {S2}")

#######################################################################################################################
#                                                    ITERATORS                                                        #
#######################################################################################################################
"""
An object that contains a countable number of values, can be iterated on meaning you can go through all the values.
It implements the iterator protocol consisting of __inter__ and __next__ methods.
"""

################################################### Iterator vs Iterable ##############################################
print(f"\n{'Iterator vs Iterable':#^65}")
"""
Data collections are all iterable objects which lets you get an interator from their containers. An iterable is
created when passed to __inter__ while an iterator iterates over an iterable using __next__. Not all iterables are
iterators, but every iterator is also an iterable.
"""

mytuple = (1, 2, 3)
myit = iter(mytuple)  # using __inter__ to get the data from the tuple container
print(f"Looping through the tuple now.....{next(myit)} {next(myit)} {next(myit)}")

"""
Uses the '__next__' to loop over the data returning the results before moving to the the next, printing '1' than
looping again to print '2' and finally looping once more to print '3'
"""

#################################################### Creating #########################################################
"""
When creating an object or class using these methods it works very similar to the method used in Lesson Twelve
letting you do operations as long it returns the iterator object, you have to also have the next item in the sequence
return to add operations using __next__.
"""


class Numbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        b = self.a
        self.a += 1
        return b


myclass = Numbers()
myiter = iter(myclass)

print(f"Creating an Iterator......{next(myiter)} {next(myiter)} {next(myiter)}")

##################################################### Stopping ########################################################
print(f"\n{'Stopping an Iterator':#^65}")
"""
The code above would run forever with if you figured out how to loop the next statement, to prevent this from
happening using the StopIteration statement is needed, by adding this to the next method it can terminate it after 
a specific amount of numbers have been done.
"""


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            b = self.a
            self.a += 1
            return b
        else:
            raise StopIteration


num = MyNumbers()
it = iter(num)

for b in it:
    b -= 1
    print(f"Counting from '0' to '19'\nStopping now at ----> {b}")

#######################################################################################################################
#                                                    INHERITANCE                                                      #
#######################################################################################################################
"""
Allows you to define a class which inherits all the other methods and properties from other classes, called a parent
and child class.
"""

###################################################### Parent and Child Class #########################################
print(f"\n{'Parent and Child Classes':#^65}")
"""
The syntax is no different for a parent class as any python class can be a parent class, to make a class able to
inherit functions from other classes, use the parent class as a parameter within the child class.
"""


class Student:  # parent class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(f"My self is {self.firstname} {self.lastname} nice to meet you!")


s = Student("Simon", "Ranger")
s.printname()


class Teacher(Student):  # child class, with parent class as the value
    pass


t = Teacher("Dean", "Smith")
t.printname()

#######################################################################################################################
#                                                  OBJECTS                                                            #
#######################################################################################################################

##################################################### Modify and Delete Properties ####################################
print(f"\n{'Modifying and Deleting Properties':#^65}")
S2.age = 18  # changes the age from "32" to "30
print(f"I don't want to be '32' anymore...lets be '18' again! by changing the value of 'S2.age' we have now become "
      f"----> {S2.age} <---- again!!!")

# del S2.age  # deletes the age property from the class and function
# del S1  # deletes the whole function
print(f"We had to comment out the 'del' part as it would throw an error, deleting the whole variable or even function!")

#######################################################################################################################
#                                               ADDING FUNCTIONS                                                      #
#######################################################################################################################

######################################################## Super ########################################################
print(f"\n{'The Super() Function':#^65}")
"""
Another function letting the child class inherit all methods and properties from the parent, by using this function
you won't need to use the self of the parent element as it automatically inherits that information.
"""


class Student3(Student):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

    def printname(self):
        print(f"Today we get another new student called {self.firstname} {self.lastname}")


s3 = Student3("Sam", "Smith")
s3.printname()

#######################################################################################################################
#                                         PROPERTIES AND METHODS                                                      #
#######################################################################################################################
print(f"\n{'Properties and Methods':#^65}")
"""
To add another property or method to a class is very easy to do, simply create a variable, pass it through the parent 
class by adding it to the __init__ function. When it comes to adding methods, all you need to do is add it to the child
class with the same self as the parents function, doing this will override the parents inheritance.

There are also properties called 'Getters' and 'Setters' which don't work the same as with other languages, which in
python is mainly used for getting validation from something.
"""


class Student4(Student):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.gradelevel = year  # adds the property "year" to the "Student4" class

    def message(self):
        return f"Everyone lets congratulate {self.firstname} {self.lastname} for passing grade {self.gradelevel}"


s4 = Student4("Bob", "Smith", 2)
print(f"{s4.message()}\n")


class Food:
    def __init__(self, options):
        self.options = options
        self._snacks_allowed = False

    @property  # this is the getter method, simply gets the value
    def snacks_allowed(self):
        return self._snacks_allowed

    @snacks_allowed.setter  # this is the setter method used to simply set the value
    def snacks_allowed(self, value):
        if value:
            password = input('Please enter the password: ')
            if password == "Hell0":
                print(f"Welcome back!")
                self._snacks_allowed = value
            else:
                raise ValueError("Intruder Alert")


food = Food(["chocolate", "cream"])
print(food.snacks_allowed)
food.snacks_allowed = True
print(food.snacks_allowed)

#######################################################################################################################
#                                                  EXERCISE                                                           #
#######################################################################################################################
print(f"\n{'Exercise Practice: Mixing Drinks':#^65}")


class Drink:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"{self.name} ({self.amount}L)"

    def __add__(self, other):
        return f"{Drink(self.name + other.name, self.amount + other.amount)}"


a = Drink('Coke & ', 1.5)
b = Drink('Pepsi', 2.0)

result = a + b
print(result)
