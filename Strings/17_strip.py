# Python lstrip() method is used to remove all leading characters from the string. It takes a char type parameter which is optional. If parameter is not provided, it removes all the leading spaces from the string.z
# str =  "  Javatpoint  "  

# str = str.strip()
# print(str)

s = "#"
str = "######ABHISHEK######"
print(str.lstrip('#'))
print(str.rstrip('#'))
print(str.strip("#"))

str = str.strip("#")
print(str.strip('A'))