def fact(n):
    f=1
    for i in range(2,n+1):
        f=f*i
    return f
n=int(input("Enter the number:"))
x=fact(n)
print("Factorial is =",x)