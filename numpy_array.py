from numpy import *
arr=array([1,2,3,4,5,6,7,8,9])
print(arr)
print("Type - ",arr.dtype)
arr1=array([1,2,3,4,5.5,6,7])
print(arr1)
print("Type - ",arr1.dtype)

#linspace()

print("Usage of linspace to make 16 parts betweeen numbers 1 and 15\n")
arr2=linspace(1,15,16)
print(arr2)

print("Usage of linspace to make 6 parts betweeen numbers 56 and 90\n")
arr3=linspace(56, 90, 6)
print(arr3)

#arange()
print("using arrange(starting,ending+1,skip)")
arr4 = arange(1, 15, 2)
print("\narrange(1,15,2) - ", arr4)

#logspace()
print("using logspace(starting,ending,no of elements)\n")
arr5 = logspace(1, 40, 5)
print("logspace(1, 40, 5) - ", arr5)

#zeros()
print("\nUsing zeros(no of elements,datatype(optional,eg:-int,float...))\n")
arr6 = zeros(5)
print("zeros(5)=", arr6)

#ones()
print("\nUsing ones(no of elements,datatype(optional,eg:-int,float...))\n")
arr7 = ones(5)
print("ones(5)=", arr7)