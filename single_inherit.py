class rect:
    area1 = 0
    def calc_area1(self,l,b):
        print("Area of the rect =",l*b)
class square(rect):
    area2 = 0
    def calc_area2(self,s):
        print("Area of the square =", s*s)
obj=square()
l= int(input("Enter the length:"))
b = int(input("Enter the breadth"))
obj.calc_area1(l,b)
obj.calc_area2(l)
