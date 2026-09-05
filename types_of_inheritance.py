#Simple Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Vehicle started.")

class Car(Vehicle):
    def reverse(self):
        print("Car is now reversing")

'''
car = Car("Tata")
car.start()
car.reverse()
'''

#Multilevel Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Vehicle started.")

class Car(Vehicle):
    def reverse(self):
        print("Car is now reversing")

class Nano(Car):
    def size(self):
        print(f"Seating size of {self.brand} is small.")

'''
n = Nano("Tata")
n.start()
n.reverse()
n.size()
'''

#Hierarchial Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"Vehicle of brand {self.brand} started.")

class Car(Vehicle):
    def reverse(self):
        print(f"Car of brand {self.brand} is now reversing")

class Bike(Vehicle):
    def kickStart(self):
        print(f"Bike of brand {self.brand} is now started manually.")

'''
car = Car("Tata")
bike = Bike("Hero")

car.start()
car.reverse()

bike.start()
bike.kickStart()
'''

#Multiple (Diamond Problem) Inheritance

class A:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from {self.name} to A")

class B(A):
    def greet(self):
        print(f"Hello from {self.name} to B")
        super().greet()

class C(A):
    def greet(self):
        print(f"Hello from {self.name} to C")
        super().greet()

class D(B, C):
    def greet(self):
        print(f"Hello from {self.name} to D")
        super().greet()

'''
print(D.mro())

d = D("Saransh")
d.greet()
'''

#Hybrid Inheritance
class A:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is speaking.")

class B(A):
    def shout(self):
        print(f"{self.name} is shouting.")

class C(A):
    def cry(self):
        print(f"{self.name} is crying.")

class D(B,C):
    def beat(self):
        print(f"{self.name} is beating.")

class E(D):
    def watch(self):
        print(f"{self.name} is watching.")

e = E("Saransh")
e.watch()
e.beat()
e.cry()
e.shout()
e.speak()
