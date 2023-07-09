# Python ljust() method left justify the string and fill the remaining spaces with fillchars. This method returns a new string justified left and filled with fillchars.

#  length of string must br 1

s = 'javatpoint'

s = s.ljust(20,"$")
print(s)

str = "abhishek verma"
length = len(str)
str = str.ljust(length+2,"d")
print(str)