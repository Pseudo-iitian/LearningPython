a = "!!!!Harry!!!!!!"
print("length of string",a,"is:",len(a))
print(a.upper())
print(a.lower())

a = a.lstrip("!")
a = a.rstrip("!")
a = "HarryAbhishek verma Harry"
print(a)
print(a.replace("Harry","Abhishek"))

b = "i am Abhishek Verma From KIET Group"
print(b.split(" "))

print(b.capitalize())

print(len(b))
print(b.center(50))

print(b.count("am"))

print(b.endswith("p"))

val = "Abhishek is a good boy and you are a bad boy"
print(val.find("isdfk",4)) #if not found that return -1

print(val.index("is")) #if not found then raise an ERROR

word = "Abhishek4322dsflkjLKDSJ"
print(word.isalnum())

letter = "Abhishek"
print(letter.isalpha())

num = "4333"
print(num.isnumeric())  

letter = "abishf!#"
print(letter.islower()) #it checks for character only 

space = "               "
print(space.isspace())

title = "Mountain Hills in thE Garden"
print(title.istitle())

letter = "Abhishek"
print(letter.startswith("Abhishek"))

print(letter.swapcase())

print(title.title())

# 14