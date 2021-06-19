from numpy import *
#aliasing
print("Aliasing")
arr1=array([11,22,33,44,55])
arr2=arr1
print("ID of arr1 =",id(arr1))
print("ID of arr2 =",id(arr2))

#shallow copy
#changes in array after copying will reflect on second array even though id is different
print("\nShallow copy")
arr3=array([11,22,33,44,55])
arr4=arr3.view()
print("ID of arr3 =",id(arr3))
print("ID of arr4 =",id(arr4))
arr3[1]=99
print("arr3=",arr3)
print("arr4=", arr4)

#deep copy
#changes in array after copying does not reflect on second array
print("\nDeep copy")
arr5=array([11,22,33,44,55])
arr6=arr5.copy()
print("ID of arr5 =",id(arr5))
print("ID of arr6 =",id(arr6))
arr5[1]=99
print("arr5=",arr5)
print("arr6=", arr6)