a=6
b=5
print(a+b)
print(int.__add__(a,b))#constructor overloading
#here both print statements does the same.

class S:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=S(m1,m2)
        return s3
s1=S(2,5)
s2=S(5,2)
s4=s1+s2
print(s4.m1)
