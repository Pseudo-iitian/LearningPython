# s = {2,4,2,6}
# print(s)

# set is a collection of distinct unique ordered collection of objects
# it does not allow repeated value
# in this ordered can't be predicted, it is not ascending or descending.
# set does not maintain order********
# info = {"Carlo",19,False, 5.9,19}
# print(info)

# harry = {2}
# print(type(harry))

s1 = {2,4,9,10,22,1}
print(s1)

s2 = {2,3,6,5,9,7}
print(s2)

# it will give sorted set
print(s2.union(s1))

# to update one set with another set
print("before update: ")
print(s1,s2)
print("After update: ")
s1.update(s2)
print(s1,s2)
print()

s2 = {2,3,6,5,9,7}
s1 = {2,4,9,10,22,1}
# for intersection of two set
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
print(s1.isdisjoint(s2))

s1 = {1,2,3}
s2 = {1,2,3,4,5}
# s1.difference_update(s2)
# print(s1)
s1.intersection_update(s2)
print(s1)
print(s1.issubset(s2))
print(s2.issuperset(s1))

s1.add(4)
print(s1)

# remove and discard
# 1- remove raise an error if not found
s1.remove(2)
print(s1)

# 2 - discard will not raise an error if not found
s1.discard(5)
print(s1)

# pop will remove the last element in the set but we don't know where but we can fetch that element
val = s1.pop()
print(s1)
print("popped value is: ",val)

del s2
# print(s2)
# s2 is not defined as it is deleted now

s1.clear()
#  clear methdo clears all the elements of the set and returns an  empty set
print(s1)