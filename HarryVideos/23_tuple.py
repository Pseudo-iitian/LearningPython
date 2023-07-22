# tuple is immutable
# this will show the tuple of type int
# comma is improtant to create a tuple with single element
tup = (1)
print(type(tuple),tup)

tup = (1,2,3,4,"green",True)
print(type(tuple),tup)

print(tup[0])
print(tup[-1])
print(tup[2])

if 2 in tup:
    print("Yes")

tup2 = tup[1:4]
print(tup2)

