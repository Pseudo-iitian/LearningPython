import time

seconds = time.time()
curtime = time.localtime(seconds)
hrs = curtime.tm_hour
min = curtime.tm_min

# good morning
if((hrs>24 or min>0) and (hrs<12 and min<=59)):
    print("Good Morning!")
elif((hrs>=12 or min>0) and (hrs<5 or min<59)):
    print("Good Afternoon!")
elif((hrs>=5 or min>0) and (hrs<9 or min<=59)):
    print("Good Evening!")
elif((hrs>=9 or min>0) and (hrs<24 or min<=59)):
    print("Good Night")




