# Docstring- Python docstring are the string literals that appear right after the definiton of a function, methods, class or module.

def square(n):
    '''It take an integer as an input and return square of it'''
    print(n**2)

square(5)
print(square.__doc__)
print(square.__code__)
print(square.__module__)

# import this
# the zen of python by tim peters
