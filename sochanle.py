def sochanle(n):
    k=str(n)
    length=len(k)
    for i in range(length):
        digit=int(k[i])
        if (i+1)%2==0:
            if digit%2!=0:
                return False
        else:
            if digit %2==0:
                return False
    return True
n=int(input())
if sochanle(n):
    print("YES")
else:
    print("NO")