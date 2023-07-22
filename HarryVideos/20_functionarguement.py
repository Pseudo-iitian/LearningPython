'''function arguement and return statement
four types

1- default arguement
2- keyword arguement
3- variable length arguement
4- required arguement
'''

# 1- default arguement
def addTwoNum(a=4,b=9):
    print("The average is: ",(a+b)/2)

addTwoNum(b=2)

# 2- keyword arguement
def name(fname,mname="Kumar",lname="Verma"):
    print("Hello!",fname,mname,lname)

name(fname = "Abhishek", lname="Soni") #here lname = "soni" -> lname is the keyword

# 3- variable length arguements
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("average: ", sum/len(numbers))

average(1,1,1,1,1)
