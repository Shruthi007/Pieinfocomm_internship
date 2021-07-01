class S:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __divmod__(self, other):
        r1=self.m1 // other.m1
        x1=self.m1 % other.m1
        r2=self.m2 // other.m2
        x2=self.m2 % other.m2
        s3 = S([r1,x1], [r2,x2])
        return s3

s1=S(20,21)
s2=S(5,5)

s4=divmod(s1,s2)
print(s4.m1[0]," ,",s4.m1[1])
print(s4.m2[0]," ,",s4.m2[1])