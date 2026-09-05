#Simple Inheritance 

#Base/Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

#Derived Class
class Dog(Animal):
    def __init__(self):
        self.color = "Black"

    def speak(self):
        print(f"The dog barks and it's color is {self.color}")

#Instance/Object of parent class
anm = Animal("Pet")
print(anm.name)
anm.speak()

#Instance/Object of child class
dg = Dog()
dg.speak()

            