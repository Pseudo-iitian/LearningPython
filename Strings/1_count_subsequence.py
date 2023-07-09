# s = input("Enter any string")
s = "javatpoint"
#     count(sub[, start[, end]])  
cnt = s.count('t')
print(cnt)

str = "ab bc ca de ed ad da ab bc ca"  
# res = str.count('a')
res = str.count('a',3,8)
print(res)

# It counts the number of occurrences of a substring in a String between begin and end index.