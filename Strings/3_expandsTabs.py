# expandtabs()
# Python expandstabs() method replaces all the characters by sepecified spaces. By default a single tab expands to 8 spaces which can be overridden according to the requirement.
# by default is 8
# It defines tabs in string to multiple spaces. The default space value is 8.
str = "welcome\tto\tkiet\tgroup\tof\tinstitutions"
print(str.expandtabs(2))
print(str.expandtabs(3))