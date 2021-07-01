#parent class
class A:
    def feature1(self):
        print("FEATURE 1")

    def feature2(self):
        print("FEATURE 2")

class B(A):
    def feature3(self):
        print("FEATURE 3")

    def feature4(self):
        print("FEATURE 4")
b=B()
b.feature1()
b.feature3()
b.feature2()
b.feature4()