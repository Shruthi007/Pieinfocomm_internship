class S:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __sub__(self, other):
        r1=self.m1-other.m1
        r2=self.m2-other.m2
        s3 = S(r1, r2)
        return s3

s1=S(20,6)
s2=S(8,9)

s4=s1-s2
print(s4.m1," ,",s4.m2)