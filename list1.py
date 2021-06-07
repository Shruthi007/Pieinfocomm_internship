#List->represented by[]
#mutable and treated as array

a=[33,55,66,9,8,7,45,8,7,55,7]

print("n=",len(a))
a.insert(3,998)
print("After insertion",a)
print("n=",len(a))
a.extend([78,54,78,96,87])
print("After inserttion",a)
print("n=",len(a))
a.pop()
print("AFter popping",a)
print("n=",len(a))
a.pop(2)
print("AFter popping 2nd indexed element",a)
print("n=",len(a))
a.sort()
print("Sorted-",a)

#reverse(),clear(),index()...


