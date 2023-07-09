str = "Java \n is a programming \r language"  

print(str.splitlines())

s = "java is\na programming\tlanguage"
print(s.splitlines())

str2 = s.splitlines(True) # returns a list having splitted elements  
print(str2)

a = " "
s = "this is a popat ganganam style"
res = s.split()
res = a.join(res)
print(res)
