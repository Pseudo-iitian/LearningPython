letter = "Hello! I am {name} and I and I am from {country}"
name = "Abhishek Verma"
country = "India"


# it is not a good approach then 
# letter = "i am {1} and I am from {0}"
# print(letter.format(name,country))
# print(letter.format(country,name))

print(f"I am a {name} and I am from {country}")

text = "for only {price: .2f} dollars"
print(text.format(price = 49.099999))

# usign f string
price = 23.3432432
txt = f"For only {price: .4f} dollars"
print(txt)

# if you want you to showcase you culry braces then
print("I am a {name} and I am from {country}")
print(f"I am a {{name}} and I am from {{country}}")