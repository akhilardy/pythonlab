i, j, flag = 0, 0, 0
primes=list()
N=int(input("ENTER NUMBER OF PRIMES TO PRINT:"))
for i in range(1,10000): 
    if (i == 1 or i == 0): 
        continue
    flag = 1; 
    for j in range(2, ((i // 2) + 1)): 
        if (i % j == 0): 
            flag = 0
            break
    if (flag == 1): 
        primes.append(i)
print(primes[:N])
