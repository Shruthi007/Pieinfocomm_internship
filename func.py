#functions
#>>user defined functions
def greet(): #no arg no return type
    print("hello")
def sum():
    a=10
    b=20
    return (a+b)
def sum1(a,b):
    print(a+b)
def sum2(a,b):
    return (a+b)
def add_sub(a,b):
    return a+b,a-b
greet()
print(sum())
sum1(4,5)
print(sum2(4,10))
c,d=add_sub(5,4)
print("sum=",c,"\ndiff=",d)