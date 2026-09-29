# Object Oriented Programming :

# Classes - 
# object - 

# class
class Student:
    # constructor
    def __init__(self, name, course, age):
      self.name = name
      self.course = course
      self.age = age 

    # methods

    def printStudentDetails(self):
        print(f"Student's name is : {self.name}")
        print(f"Student's age is : {self.age}")
        print(f"Student's course is : {self.course}")

# instance/object

student1 = Student("Rohan", "B.Tech AIML", 20)
student2 = Student("Mohan", "B.Tech Cyber security", 21)

# print(student1)
student1.printStudentDetails()






    
