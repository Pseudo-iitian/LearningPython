# Python partition() method splits the string from the string specified in parameter. It splits the string from at the first occurrence of parameter and returns a tuple. The tuple contains the three parts before the separator, the separator itself, and the part after the separator.

s = "Ravi is a good boy"

str = s.partition("is")
print(str)

str1 = s.partition("Ravi".capitalize())
print(str1)

str2 = s.partition('a')
print(str2)

abc = "Java is a programming language"
print(abc.partition("not"))
