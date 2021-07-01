class S:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __le__(self, other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if(r1<=r2):
            return True
        else:
            return False
s1=S(20,6)
s2=S(21,6)
if s1<=s2:
    print("s1 wins")
else:
    print("s2 wins")
