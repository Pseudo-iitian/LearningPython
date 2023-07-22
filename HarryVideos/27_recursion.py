# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)

# fact = int(input("Enter a number: "))
# print("factorial of a number is; ",factorial(fact))


# for fibonacci series
def fib(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return fib(n-1)+fib(n-2)

num = int(input("Enter n: "))
for i in range(num):
    print(fib(i))