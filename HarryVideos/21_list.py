# list by code with harry

li = [1,2,3,4,5]
print(li)
print(type(li))

for i in li:
    print(i,end=" ")

print("")
print(li[0])
print(li[1])
print(li[2])
print(li[3])
print(li[4])
print()
# print(li[5])  it will give erro

# Negative Indexing
print(li[-3])
print(li[len(li)-3])
print(li[5-3])
print(li[2])

# in keyword
if 1 in li:
    print("Yes")
else:
    print("No")

# string 
a = "abhsihek verma"
if "abhi" in a:
    print("YES")
else:
    print("No")

marks = [1,2,3,'harry',True]
print(marks[1:])
print(marks[1:-1])
print(marks[1:len(marks)-1])

# jump index
print(marks[1:len(marks):2])

# List Comprehension
list = [i*i for i in range(10) if i%2==0]
print(list[:])
