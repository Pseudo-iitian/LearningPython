# Python isprintable() method returns True if all characters in the string are printable or the string is empty. It returns False if any character in the string is Nonprintable.

s = "abhishek#@!%^&*()"
print(s.isprintable())

s1 = "fds\t"
print(s1.isprintable())

s2 = "ffds\n"
print((s2.isprintable()))

s3 = "dgh;"
print(s3.isprintable())

s4 = "sdfjakl\'"
print(s4.isprintable())