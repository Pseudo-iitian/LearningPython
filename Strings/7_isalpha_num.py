# Python isalnum() method checks whether the all characters of the string is alphanumeric or not. A character which is either a letter or a number is known as alphanumeric. It does not allow special chars even spaces.


# It returns either True or False.

str = "welcome"
s = "311431e"
st = 'weolc#@'
num = "1234134"

print(str.isalnum())
print(s.isnumeric())
print(s.isalpha())
print(st.isalnum())

print(num.isnumeric())
print(num.isascii)

space = "   "
print(space.isspace())

res = "3132"
print(res.isdigit())
print(res.isdecimal())

print(s.isnumeric())