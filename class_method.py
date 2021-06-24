class Student:
    school = "cvk"#static variable
    def __init__(self,m1,m2,m3): #instance method
        self.m1 = m1
        self.m2 = m2  # instance variable
        self.m3 = m3

    def avg(self):  # instance method
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod #decorator
    def scl(cls): #class method
        return cls.school

    @staticmethod #to print details of a class
    def info():
        print("This is student class")

s1=Student(33,44,88)
print(s1.avg())
print(Student.scl())
Student.info()