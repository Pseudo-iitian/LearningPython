


# s = input("Enter any string: ")
# s = "BANANA"
# print(s[:])
# print(s[1:4])
# print(s[::2])
# print(s[-1:-5:-1])
# # print(s[-1:-5:1]) -> print blank empty string
# s = "HELLO"
# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])

# s = 'JAVATPOINT'
# print(s[-1])
# print(s[-3])
# print(s[-4:-1])
# print(s[-7:-2])
# print(s*3)
# print(s+s)
# print('V' in s)

# escape sequence charachter
# print("helo! 'kaise ho bhai?' \" ")

s = "abhiSHEK"
# It capitalizes the first character of the String and rest small. This function is deprecated in python3
print(s.capitalize()) 

# python Casefold() method returns a lowercase copy of the string.
print(s.casefold())

#Python center() method alligns string to the center by filling paddings left and right of the string
#     center(width[,fillchar])  
# method 1
print(s.center(20))
# method 2
# char fill
print(s.center(20,'$'))


