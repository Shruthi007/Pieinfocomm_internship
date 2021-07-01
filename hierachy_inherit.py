class figure:
    s,l,b,base,h=0.0, 0.0 , 0.0,0.0,0.0
    def acc1(self):
        self.s = float(input("Enter the side:"))


    def acc2(self):
        self.l = float(input("Enter the length:"))
        self.b = float(input("Enter the breadth:"))


    def acc3(self):
        self.base = float(input("Enter the base:"))
        self.h = float(input("Enter the height:"))

class square(figure):
    area1 = 0
    def calc_area1(self,s):
        self.area1 = s*s

class rect(figure):
    area2 = 0
    def calc_area2(self,l,b):
        self.area2=l*b

class tri(figure):
    area3 = 0
    def calc_area3(self,b,h):
        self.area3 = 0.5*b*h
obj1 = square()
obj2 = rect()
obj3 = tri()
ch = int(input("Enter the shape you want(square - 1,rectangle - 2, triangle - 3) :"))
if ch == 1:
    obj1.acc1()
    obj1.calc_area1(obj1.s)
    print(obj1.area1)
elif ch == 2:
    obj2.acc2()
    obj2.calc_area2(obj2.l, obj2.b)
    print(obj2.area2)
else:
    obj3.acc3()
    obj3.calc_area3(obj3.base,obj3.h)
    print(obj3.area3)


