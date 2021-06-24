class Computer:
    def __init__(self,cpu,ram):
        print("In init")  # default constructor
        self.cpu=cpu
        self.ram = ram

    def sum(self):
        print("config:",self.cpu,self.ram)


c = Computer("cpu1","ram1")
c1 = Computer("cpu2","ram2")

c.sum()
c1.sum()
# each time object is created default constuctor is called