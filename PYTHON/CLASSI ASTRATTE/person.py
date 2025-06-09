from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name:str, age:int) ->None:
        
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self) ->str:
        pass

    def __str__(self) ->str:
        
        return f"Name:{self.name}, Age:{self.age}, Role:{self.get_role()}"
    

class Courses:

    def __init__(self):
        pass

class Department:

    def __init__(self):
        pass

class Student(Person):

    def __init__(self, name:str, age:int, studentID:str):
        super().__init__(name, age)

        self.studentID:str = studentID
        self.courses:list[Courses] = []


    def get_role(self) ->str:
        
        return "Student"
    
    def enroll(self) ->None:

        pass

class Professor(Person):

    def __init__(self, name:str, age:int, professorID:str, department:Department):
        super().__init__(name, age)

        self.professorID:str = professorID
        self.department:Department = department
        self.courses:list[Courses] = []

    def get_role(self) ->str:
        return "Professor"

