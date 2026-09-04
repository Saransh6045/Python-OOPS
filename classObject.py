#creating a class
class Student:

    #special method/magic method/dunder method -> constructor to define data/attributes
    def __init__(self):
        print("Initializing the class object")
        self.name = "Saransh"
        self.id = 101
        self.marks = 90
        print("Object initialized successfully")

    #Inializing a method
    def displayPercentage(self, totalMarks):
        percentage = self.marks / totalMarks * 100
        print("Percentage of student is: ", percentage, "%")

#Creating an object of the class
student = Student()
student.country = "India"
print(student.country)

#Running the method manually
#student.displayPercentage(100)
