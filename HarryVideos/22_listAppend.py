l = [1,2,3,4,6]
print(l)
l.append(9)
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print("index of 6 is :",l.index(6))
print("count of 3 is: ",l.count(3))

m = l # where m = 1
m[0]=0
print(l)

m = l.copy()
m[0]=0
print(l)

# inserting at middle
l.insert(1,99)
print(l)


# merge two list to another
m = [10,11,12]
k = l + m
print(k)

# m ko kholo then l me concatenate kr do 
l.extend(m)
print(l)