class Student:
    """
    A class that represents a student
    """
    def __init__ (self, theName, theGrade, theClass):
        """
        Store the parameters as class variables
        """
        self.name = theName
        self.grade = theGrade
        self.className = theClass
        
    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName
    
    def getClass(self):
        return self.className
    
    def setClass(self, newClass):
        self.className = newClass

    def getGrade(self):
        return self.grade
    
    def setGrade(self, newGrade):
        self.grade = newGrade
