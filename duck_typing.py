class pycharm:
    def execute(self):
        print("Compiling")
        print("Running")
class MyEditor:
    def execute(self):
        print("spell check")
class Laptop:
    def code(self,ide):
        ide.execute()
ide1=pycharm()
l1=Laptop()
l1.code(ide1)
