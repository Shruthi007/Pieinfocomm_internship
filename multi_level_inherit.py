class figure:
    l,b=0,0
    def acc(self):
        self.l = int(input("Enter the length: "))
        self.b = int(input("Enter the breadth: "))

class rect(figure):
    area1 = 0
    def calc_area1(self):
        self.area1=self.l*self.b
class square(rect):
    area2 = 0
    def calc_area2(self):
        self.area2=self.l*self.l
obj=square()
obj.acc()
obj.calc_area1()
obj.calc_area2()
print("Area of rect = ",obj.area1)
print("Area of square = ",obj.area2)
