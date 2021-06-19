from numpy import *
arr1=array([[44,55,22],[77,88,99],[22,11,33],[55,99,77]])
print(arr1)
print("Datatype :", arr1.dtype)
print("Dimension:", arr1.ndim)
print("Order of array:", arr1.shape)
print("No of elements:", arr1.size)

#flattening
print("\nFlattening")
arr2=arr1.flatten()
print(arr2)
print("\nReshaping")
arr3 = arr2.reshape(6,2)
print(arr3)