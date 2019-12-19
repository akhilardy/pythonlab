n=int(input("enter size:"))
l=list()
for i in range(n):
    k=int(input())
    l.append(k)
beg=int(input("begin offset:"))
end=int(input("end offset:"))
asc=l[beg:end]
desc=l[0:beg]+l[end:]
asc.sort()
desc.sort()
ans=list()
off=int(0)
on=len(desc)-1
for k in range(len(l)):
    if k in range(beg,end):
        ans.append(asc[off])
        off=off+1
    else:
        ans.append(desc[on])
        on=on-1
print(ans)
