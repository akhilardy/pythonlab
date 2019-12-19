print("enter date of birth:")
n=int(input())
print("enter present year:")
p=int(input())
l=list(range(n,p))
age=len(l)
leap=list()
for i in l:
    if i%4==0:
        if  i%100==0 and i%400!=0:
            continue
        else:
            leap.append(i)
decades=list()
for i in l:
    if i%10==0:
        decades.append(i)
print("age is:",age)
print("number leap years are:",len(leap)," and they are:",leap)
print("number of decades are:",len(decades)," and they are:",decades)
print("year   age")
k=int(0)
for i in l:
    print(i,"   ",k)     
    k=k+1
print(p,"   ",age)
            
            
