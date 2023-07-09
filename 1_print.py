name = "John"
age = 25

print(name, age, sep=' - ', end='!', flush=True)
# print(name, age, sep=' - ', end='!', file=sys.stdout, flush=True)

# use of flush 
import time
# # by default flush is false
print("Hello", end='', flush= False)
time.sleep(2)  # Delay for 2 seconds
print(" World!")

# use of flush is true
print("Hello", end='', flush= True)
time.sleep(2)  # Delay for 2 seconds
print(" World!")