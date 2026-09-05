class Animal:
    def __init__(self):
        self.name = "Sheru"

    def speak(self):
        print(f"{self.name} makes the sound")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.breed = "German Shepherd"

    def speak(self):
        super().speak()
        print(f"{self.name} is a {self.breed} and has a sound.")


anm = Animal()
anm.speak()

dg = Dog()
dg.speak()
    