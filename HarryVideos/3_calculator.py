print("Created A Calculator")
print("""You can do only : 
      1- Addition
      2- Subtraction
      3- Multiplication
      4- Division
      5- Modulo
      6- square""")

a = int(input("Enter a: "))
o = input("Enter Operator: ")
b = int(input("Enter b: "))

# calculator using match and case in python
match o:
    case "+":
        print("sum of {} and {} is: {}".format(a,b,a+b))
    case "-":
        print("subtraction of {} and {} is: {}".format(a,b,a-b))
    case "*":
        print("multiplication of {} and {} is: {}".format(a,b,a*b))
    case "/":
        print("division of {} and {} is: {}".format(a,b,a//b))
    case "%":
        print("modulo of {} and {} is: {}".format(a,b,a%b))
    case "square":
        print("{} to the power of {} is: {}".format(a,b,a**b))