#Set -> Datatype similar to set in maths
#Doesnot support duplication and indexing
# Represented useing {}
# output is always in random order
a={1,6,5,8,7,9,4,11,5,6,6}
print("a=",a)
b={1,5,7,8,9,4,6,8,10,5}
print("b=",b)
print("a-b=",a.difference(b))
print("a U b=",a.union(b))
print("a intersection b =",a.intersection(b))
