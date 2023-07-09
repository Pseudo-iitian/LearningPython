# Python rsplit() method seperates the string and returns a list. It splits from the right using seperator as a delimiter. If seperator is not specified, any whitespace string is a separator. This method does same as split() except splitting from the right which is described in detail below.

str = "Java is a programming language"  
list = str.rsplit()
print(list)

print(str.rsplit('java'))

print(str.rsplit('a'))  

# str.rsplit(value,count) split from right end

print(str.rsplit('a',1))
print(str.rsplit('a',3))