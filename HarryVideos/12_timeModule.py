import time

seconds = time.time()
print("Seconds since epoc(the point where time begin): ", seconds)

time.sleep(1)
#  localt time Tue Jul 18 12:35:43 2023
local_time = time.ctime(seconds)
print("Local Time: ",local_time)

# The localtime() function takes the number of seconds passed since epoch as an argument and returns struct_time (a tuple containing 9 elements corresponding to struct_time) in local time.
local_time = time.localtime(seconds)
print("9 elements containing exact current time: ",local_time)
print("year: ",local_time.tm_year)
print("Month: ",local_time.tm_mon)
print("Day: ",local_time.tm_mday)
print("Day: ",local_time.tm_wday)
print("Day: ",local_time.tm_yday)

# The gmtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in UTC.

local_time = time.gmtime(seconds)
print("9 elements containing exact current time: ",local_time)
print("year: ",local_time.tm_year)
print("Month: ",local_time.tm_mon)
print("Day: ",local_time.tm_mday)
print("Day: ",local_time.tm_wday)
print("Day: ",local_time.tm_yday)


# The mktime() function takes struct_time (a tuple containing 9 elements corresponding to struct_time) as an argument and returns the seconds passed since epoch in local time.

tuple = local_time
seconds = time.mktime(tuple)
print("Seconds sine epoc: ",seconds)

# In Python, the asctime() function takes struct_time as an argument and returns a string representing it.
# it also takes tuple
samaye = time.asctime(tuple)
print("time in string : ",samaye)


# The strftime() function takes struct_time (or tuple corresponding to it) as an argument and returns a string representing it based on the format code used. For example,

# time.strftime()
tuple_time = time.localtime()
time_string = time.strftime("%m/%d/%Y, %H/%M/%S", tuple_time)
print(time_string)

# # The strptime() function parses a string representing time and returns struct_time.
time_string = "2023-07-18 10:30:00"
result = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print(result)

