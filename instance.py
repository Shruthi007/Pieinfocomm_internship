class Student:
    school = "cvk"#static variable
    def __init__(self,m1,m2,m3): #instance method
        self.m1=m1
        self.m2=m2 #instance variable
        self.m3=m3

    def avg(self): #instance method
        return (self.m1+self.m2+self.m3)/3

s1=Student(33,44,88)
print(s1.avg())