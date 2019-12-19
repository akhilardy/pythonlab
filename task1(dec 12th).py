import random
n=int(input("enter a number:"))
n1=random.randrange(10000)
if n1>n:
    print(n,":is too low  than:",n1)
elif n1<n:
    print(n,":too high than:",n1)
else :
    print(n,":matching:",n1)
