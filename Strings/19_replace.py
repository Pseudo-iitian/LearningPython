s = "java is a good language"

# s.replace(old,new,count)
# if no count mention, replace all the occurence of c++ or new string
s = s.replace("java","c++")
print(s)

str = "python is way python python python easy language"
str1 = str.replace("python","java")
print("Replacing all occurence: ",str1)

str2 = str.replace("python","c++",1)
print("replacing only one occurence: ", str2)

# we can alos replace all string with another string

a = "this is abhishek verma from your college"
a = a.replace(a,"i am a good boy and my name is abhishek verma")
print(a)
