from array import *
arr = array('i',[])
n = int(input("Enter the size of the array:"))
for i in range(n):
    x = int(input("enter element:"))
    arr.append(x)
print(arr)
val = int(input("Enter the element to be searched:"))
flag=0
for i in arr:
    if val == i:
        print("Element is present in the array")
        flag=1
        break
if flag == 0:
    print("Element is not present in the array")