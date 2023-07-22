countries = ("Russia","Uganda","Ukraine","India","USA")
temp = list(countries)
temp.append("China")

# poping the first clememt i.e. countries[0] = Russia
temp.pop(0)

# inserting element at index 0 i.e. Nagaland
temp[0]="Australia"
temp.insert(0,"Nagaland")
print(temp)

print()

print(countries)
countries = tuple(temp)
print(countries)


print()
tuple = (1,2,1,1,1,1,12,2,3,3,3,3,3,)
print("count of 1 is:",tuple.count(1))
print()

# use of index(value,start,end) - if not found then raise an value error
print("3 (first occurence) is present at:",tuple.index(3))
res = tuple.index(3,2,len(tuple))
print(res)

