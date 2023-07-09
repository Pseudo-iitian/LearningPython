# isspace() method returns true for all whitespaces like:

    # ' ' - Space
    # '\t' - Horizontal tab
    # '\n' - Newline
    # '\v' - Vertical tab
    # '\f' - Feed
    # '\r' - Carriage return

# Python isspace() method is used to check space in the string. It returna true if there are only whitespace characters in the string. Otherwise it returns false. Space, newline, and tabs etc are known as whitespace characters and are defined in the Unicode character database as Other or Separator.

str = "abhi kldf dsf"
print(str.isspace())

s1 = " v v v "
print(s1.isspace())

s2 = "   "
print(s2.isspace())

s3 = "\t"
print(s3.isspace())

s4 = "\n"
s5 = "\v"
s6 = "\f"
s7 = "\r"

print(s4.isspace())
print(s5.isspace())
print(s6.isspace())
print(s7.isspace())