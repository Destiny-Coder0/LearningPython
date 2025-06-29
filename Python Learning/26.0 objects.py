#This is all about objects
from datetime import date
class Person:
    #class attributes
    address = "No information"

    #constructor
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
    #instance methods
    def intro(self):
        print(f"Hello there. I'm {self.name}" )

    def calculateAge(self):
        return date.today().year-self.year

#object(instance)
p1 = Person(name = "Ally", year = 1990)
p2 = Person(name = "Leila", year = 1995)

p1.intro()
p2.intro()

print(f"My name is {p1.name} and I'm {p1.calculateAge()} years old.")
print(f"My name is {p2.name} and I'm {p2.calculateAge()} years old.")


class Circle:
    #class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius=radius

    #Methods
    def calculateCircum(self):
        return 2*self.pi*self.radius
        
    def calculateArea(self):
        return self.pi*(self.radius**2)
        
c1 = Circle()
c2 = Circle(5)

print(f"c1's area = {c1.calculateArea()}, c1's circumference = {c1.calculateCircum()}")
print(f"c2's area = {c2.calculateArea()}, c2's circumference = {c2.calculateCircum()}")