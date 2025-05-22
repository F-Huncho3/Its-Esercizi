class Student:

    def __init__(self,name:str,studyProgram:str,gender:str,age:int):

        self.name = name
        self.studyProgram = studyProgram
        self.gender = gender
        self.age = age

    def printInfo(self):

        print (f"NOME:{self.name}")
        print (f"PERCORSO:{self.studyProgram}")    
        print (f"SESSO:{self.gender}")      
        print (f"ETÀ:{self.age}")


student_1 = Student ("Genoveffa", "Medicina", "Femmina", 21)
student_2 = Student ("Becco", "Giurisprudenza", "Maschio", 19)
student_3 = Student ("Andrea", "Fisioterapia", "Femmina", 22)

student_1.printInfo()
student_2.printInfo()
student_3.printInfo()

    
       
