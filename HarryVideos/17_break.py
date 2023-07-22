

n = int(input("Enter n: "))
for i in range(1,11):
    if(i==10):
        print("Skipp the iteration")
        continue
    print("{} X {} = {}".format(n,i,n*i))


for i in range(1,12):
    if(i==5):
        break;
    else:
        print(i)

print("loop ko chor kar bahar aa gya hoon")