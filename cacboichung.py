m,n=map(int,input().split())
mxn=m*n
res=[]
for i in range(1,mxn+1):
    if i%n==0:
        res.append(i)
print(*res)