class Room:
    area = 0
    def cal_area(self):
        l=int(input("Enter the length of the room in metre:"))
        b= int(input("enter the breadth of the room in metre:"))
        self.area=l*b


class Cost:
    cost=0.0
    def acc(self):
        self.cost = float(input("Enter the cost for paining one square metre:"))
class painting(Room,Cost):
    final = 0.0
    def final_calc(self):
        self.final= self.area*self.cost

obj=painting()
obj.cal_area()
obj.acc()
obj.final_calc()
print("Cost=",obj.final)
