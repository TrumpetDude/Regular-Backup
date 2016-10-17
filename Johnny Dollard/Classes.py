# Writing a class with methods

class Student:
    def __init__ (self, theName, theGrade, theClass):
        self.name = theName
        self.grade = theGrade
        self.className = theClass
        
    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName

    def getGrade(self):
        return self.grade
    
    def setGrade(self, newName):
        self.name = newName


student1 = Student("Sarah", 12, "Math")
student2 = Student("Tim", 11, "Comp Sci")

print("Example class")
print(student1.name)
print(student2.name)
student1.setName("Ellen")
print(student1.name)
print(student1.getName())#This is better

print("Example class")
print(student1.grade)
print(student2.grade)
student1.setGrade("Ellen")
print(student1.grade)
print(student1.getGrade())#This is better



# Forgetting to use self.variable

class OtherStudent:
    def __init__ (self, theName, theGrade, theClass):
        self.name = theName
        self.grade = theGrade
        self.className = theClass
        
    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName#self.name vs name


student3 = OtherStudent("Amber", 12, "Math")
print("\n\nExample setName without using self.name")
print(student3.getName())
student3.setName("Victoria")
print(student3.getName())
