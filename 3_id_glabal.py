# id 
a = b = 10
# a is like a pointer then a will point to 10 and b also point to 10, both will have same id

print(id(a))
print(id(b))

# use of global varibal in a funciton
a = 100
def prnt():
    # making a as global variable
    global a  
    # local variable has more preference 
    print("helo ji ",a)

prnt()

# deleting the variable
x = 10
del x
# print(x)
# x is not defined 
# Python doesn't have any special data type to store larger numbers.

# we can print single variable as well as multiple variables
a = 10
b = 20
print(a,b)
print(1,2,3,4,5,6)