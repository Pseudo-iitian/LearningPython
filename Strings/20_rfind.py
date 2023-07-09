# Python rfind() method finds a substring in in the string and returns the highest index. It means it returns the index of most righmost matched subtring of the string. It returns -1 if substring not found.

s = "abishek verma from kiet group of institutions, ghaziabad"
#     rfind(sub[, start[, end]])  

index = s.rfind("kiet")
print(index)

s = "It is tutorial tutorial"
ind = s.rfind("tutorial")
ind = s.rfind("t")
print(ind)
print(len(s))   